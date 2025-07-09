from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, func
from app.database import Base

class PromptHistory(Base):
    __tablename__ = "prompt_history"

    id = Column(Integer, primary_key=True, index=True)
    user_role = Column(String(50))
    prompt = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    timestamp = Column(TIMESTAMP(timezone=True), server_default=func.now())
