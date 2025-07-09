from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.mcp.tools import BookAppointmentInput, book_appointment

router = APIRouter()

@router.post("/test/book")
def test_book_appointment(input: BookAppointmentInput, db: Session = Depends(get_db)):
    return {"result": book_appointment(input, db)}
