from sqlalchemy.orm import Session
from app.orm_models import Appointment, Doctor

def create_appointment(db: Session, data): # functions to call appointment routes
    appt = Appointment(**data.dict())
    db.add(appt)
    db.commit()
    db.refresh(appt)
    return appt

def get_appointments(db: Session, filters):
    q = db.query(Appointment)
    if filters.doctor_id:
        q = q.filter(Appointment.doctor_id == filters.doctor_id)
    
    return q.all()
