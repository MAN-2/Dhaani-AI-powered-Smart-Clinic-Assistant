from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.orm_schemas.appointment import AppointmentCreate, AppointmentRead
from app.crud.appointment import create_appointment, get_appointments
from app.database import SessionLocal
from app.models import Appointment
router = APIRouter(prefix="/appointments", tags=["appointments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AppointmentRead, status_code=status.HTTP_201_CREATED)
def schedule(appt: AppointmentCreate, db: Session = Depends(get_db)):
    # pre-check doctor exist & availability omitted for brevity
    return create_appointment(db, appt)

@router.get("/", response_model=list[AppointmentRead])
def list_all(
    doctor_id: str = None, patient_email: str = None, db: Session = Depends(get_db)
):
    class F: pass
    filters = F()
    filters.doctor_id = doctor_id
    filters.patient_email = patient_email
    return get_appointments(db, filters)
@router.delete(
    "/{appointment_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete an appointment by ID"
)
def delete_appointment(
    appointment_id: str,
    db: Session = Depends(get_db)
):
    """
    Delete the appointment with the given UUID.
    Returns HTTP 204 No Content on success.
    """
    appt = db.get(Appointment, appointment_id)
    if not appt:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Appointment not found"
        )

    db.delete(appt)
    db.commit()
    