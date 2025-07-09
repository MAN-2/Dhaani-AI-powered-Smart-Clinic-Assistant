from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.orm_schemas.doctor import DoctorCreate, DoctorRead
from app.crud.doctor import create_doctor, get_doctors, delete_doctor
from app.database import SessionLocal

router = APIRouter(prefix="/doctors", tags=["doctors"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=DoctorRead, status_code=status.HTTP_201_CREATED)
def add_doctor(doctor: DoctorCreate, db: Session = Depends(get_db)):
    return create_doctor(db, doctor)

@router.get("/", response_model=list[DoctorRead])
def list_all(db: Session = Depends(get_db)):
    return get_doctors(db)

@router.delete("/{doc_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove(doc_id: str, db: Session = Depends(get_db)):
    delete_doctor(db, doc_id)
