from pydantic import BaseModel
from uuid import UUID
from typing import List

class DoctorCreate(BaseModel):
    name: str
    specialization: str
    availability: List[str]

class DoctorRead(DoctorCreate):
    id: UUID

    model_config = {"from_attributes": True}
