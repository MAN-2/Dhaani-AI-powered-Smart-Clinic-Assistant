from sqlalchemy.orm import Session
from app.orm_models import Doctor
# Doctor create , list and delete operations  
def create_doctor(db: Session, data):
    doc = Doctor(**data.dict())
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc

def get_doctors(db: Session):
    return db.query(Doctor).all()

def delete_doctor(db: Session, doctor_id):
    doc = db.get(Doctor, doctor_id)
    if doc:
        db.delete(doc)
        db.commit()
