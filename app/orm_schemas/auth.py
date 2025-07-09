# app/schemas/auth.py
from pydantic import BaseModel, EmailStr
from uuid import UUID
from typing import Literal, Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: Literal["doctor", "patient"]

class UserRead(BaseModel):
    id: UUID
    email: EmailStr
    role: str

    model_config = {"from_attributes": True}

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: Optional[UUID] = None
