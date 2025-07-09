from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import datetime

class AppointmentCreate(BaseModel): 
    doctor_id: UUID
    patient_email: str
    reason: Optional[str]
    date_time: datetime

class AppointmentRead(AppointmentCreate):
    id: UUID
    date_time: datetime
    model_config = {"from_attributes": True}
