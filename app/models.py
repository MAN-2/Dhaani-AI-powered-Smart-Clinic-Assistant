from sqlalchemy import Column, String, DateTime, ForeignKey, Text , ARRAY , func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ARRAY
from app.database import Base
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import Column, String
import uuid
from sqlalchemy.dialects.postgresql import UUID


class Doctor(Base):
    __tablename__ = 'doctors'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    specialization = Column(String, nullable=False)
    availability =  Column(
        ARRAY(String),
        nullable=False,
        default=list)    
        

    appointments = relationship("Appointment", back_populates="doctor")


class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    doctor_id = Column(UUID(as_uuid=True), ForeignKey("doctors.id"))
    patient_email = Column(String, nullable=False)
    reason = Column(Text)
    date_time = Column(DateTime, nullable=False)
    status = Column(String, default="booked")

    doctor = relationship("Doctor", back_populates="appointments")


class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False)     
    created_at = Column(DateTime(timezone=True), server_default=func.now())