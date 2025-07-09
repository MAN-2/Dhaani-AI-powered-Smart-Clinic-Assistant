

from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.mcp.tools import send_confirmation_email


import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

db: Session = SessionLocal()

result = send_confirmation_email(
    patient_email="youremail@gmail.com",
    patient_name="John",
    doctor_name="Ahuja",
    date="2025-07-07",
    time="10:00"
)

print("EMAIL SENT RESULT:", result)
