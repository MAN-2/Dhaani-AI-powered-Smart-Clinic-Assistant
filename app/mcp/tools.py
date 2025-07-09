

from typing import List , Optional
from datetime import datetime, timedelta
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import and_

from app.models import Doctor, Appointment
from uuid import uuid4
from dateutil.parser import parse

from app.mcp.tool import tool  

from app.services.email_s import send_email  
from app.services.calender_service import add_event_to_calendar


class AvailabilityInput(BaseModel):
    doctor_name: str
    date: str


@tool #Tool definition and calling
def check_doctor_availability(input: AvailabilityInput, db: Session) -> List[str]:
    doctor = db.query(Doctor)\
        .filter(Doctor.name.ilike(f"%{input.doctor_name.strip()}%"))\
        .first()
    if not doctor:
        return [f"No doctor found with name like '{input.doctor_name}'"]

    try:
        start_str, end_str = doctor.availability.split("-")
        start_time = datetime.strptime(start_str.strip(), "%H:%M").time()
        end_time = datetime.strptime(end_str.strip(), "%H:%M").time()
    except:
        return [f" Invalid availability format: {doctor.availability}"]

    base_date = datetime.strptime(input.date, "%Y-%m-%d")
    slots = []
    current_time = datetime.combine(base_date, start_time)
    end_datetime = datetime.combine(base_date, end_time)
    while current_time < end_datetime:
        slots.append(current_time.strftime("%H:%M"))
        current_time += timedelta(hours=1)

    booked = db.query(Appointment).filter(
        and_(
            Appointment.doctor_id == doctor.id,
            Appointment.date_time >= base_date,
            Appointment.date_time < base_date + timedelta(days=1),
            Appointment.status != "cancelled"
        )
    ).all()
    booked_times = {appt.date_time.strftime("%H:%M") for appt in booked}
    return [s for s in slots if s not in booked_times] or ["❌ No free slots available"]


class RescheduleInput(BaseModel):
    appointment_id: int
    new_time: str


@tool
def reschedule_appointment(input: RescheduleInput) -> str:
    return f"✅ Appointment {input.appointment_id} rescheduled to {input.new_time}."


class BookAppointmentInput(BaseModel):
    doctor_name: str
    patient_email: str
    reason: str
    date: str        # Format: "YYYY-MM-DD"
    time: str        # Format: "HH:MM"


@tool
@tool
def book_appointment(input: BookAppointmentInput, db: Session) -> str:
    doctor = db.query(Doctor)\
        .filter(Doctor.name.ilike(f"%{input.doctor_name.strip()}%"))\
        .first()
    if not doctor:
        return f"❌ No doctor found with name '{input.doctor_name}'"

    try:
        dt = parse(f"{input.date} {input.time}")
    except Exception:
        return "❌ Couldn't parse the provided date and time. Use YYYY-MM-DD and HH:MM."

    existing = db.query(Appointment).filter(
        Appointment.doctor_id == doctor.id,
        Appointment.date_time == dt,
        Appointment.status != "cancelled"
    ).first()
    if existing:
        return f"❌ That slot ({input.time}) is already booked for {input.date}."

    appt = Appointment(
        id=uuid4(),
        doctor_id=doctor.id,
        patient_email=input.patient_email,
        reason=input.reason,
        date_time=dt,
        status="booked"
    )
    db.add(appt)
    db.commit()
    db.refresh(appt)

    # 📅 Add to calendar
    try:
        event_link = add_event_to_calendar(
            doctor_name=doctor.name,
            patient_email=input.patient_email,
            reason=input.reason,
            date=input.date,
            time=input.time
        )
    except Exception as e:
        event_link = "❌ Failed to add to calendar: " + str(e)

    # 📧 Send confirmation email
    try:
        send_email(
            to_email=input.patient_email,
            subject=f"Appointment with Dr. {doctor.name} confirmed",
            body=f"Hi,\n\nYour appointment is booked with Dr. {doctor.name} at {input.time} on {input.date}.\n\n{event_link}\n\nRegards,\nMCP Assistant"
        )
    except Exception as e:
        event_link += f"\n⚠️ Email failed: {str(e)}"

    # ✅ Final return
    return (
        f"✅ Appointment booked with Dr. {doctor.name} on {input.date} at {input.time}.\n"
        f"📅 Calendar Event: {event_link}"
    )




@tool
def send_confirmation_email(
    patient_email: str,
    patient_name: str,
    doctor_name: str,
    date: str,
    time: str
) -> dict:
    """
    Sends a confirmation email to the patient after booking.
    """
    subject = f"Appointment Confirmed with Dr. {doctor_name}"
    body = f"""Hi {patient_name},

Your appointment with Dr. {doctor_name} is confirmed.

🗓 Date: {date}
⏰ Time: {time}

Regards,
MCP Smart Assistant
"""
    return send_email(to_email=patient_email, subject=subject, body=body)

""""""""""""""""""
"pt2 summary gen"
from uuid import UUID 
def generate_summary_report(
    doctor_id: str,
    start_date: Optional[str] = None,  # format: 'YYYY-MM-DD'
    end_date: Optional[str] = None,    # format: 'YYYY-MM-DD'
    db: Session = None
) -> str:
    """
    Generate a summary report for a doctor between start_date and end_date.
    If dates are not provided, defaults to last 30 days.
    """

    if not db:
        return " Database session not provided."

    # Convert doctor_id to UUID
    try:
        doctor_uuid = UUID(doctor_id)
    except ValueError:
        return "Invalid doctor_id format. Must be a valid UUID string."

    # Parse dates
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d") if start_date else datetime.now() - timedelta(days=30)
        end = datetime.strptime(end_date, "%Y-%m-%d") if end_date else datetime.now()
    except ValueError:
        return " Invalid date format. Use YYYY-MM-DD."

    # Query appointments
    appointments = db.query(Appointment).filter(
        Appointment.doctor_id == doctor_uuid,
        Appointment.date_time >= start,
        Appointment.date_time <= end
    ).all()

    if not appointments:
        return "No appointments found in this date range."

    # Generate summary
    summary_lines = [
        f"📝 Doctor Summary Report ({start_date or 'last 30 days'} to {end_date or 'now'})",
        "-" * 40
    ]

    for appt in appointments:
        summary_lines.append(
            f"📅 {appt.date_time.strftime('%Y-%m-%d %H:%M')} - {appt.patient_email} ({appt.reason})"
        )

    return "\n".join(summary_lines)