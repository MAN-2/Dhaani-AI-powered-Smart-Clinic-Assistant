from fastapi import APIRouter
from app.mcp.tools import send_confirmation_email

router = APIRouter()

@router.post("/test/send-email")
def test_email():
    result = send_confirmation_email(
        patient_email="youremail@gmail.com",
        patient_name="John",
        doctor_name="Ahuja",
        date="2025-07-07",
        time="10:00"
    )
    return {"status": "sent", "result": result}
