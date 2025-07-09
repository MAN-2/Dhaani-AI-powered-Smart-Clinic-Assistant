from pydantic import BaseModel
from datetime import datetime

class PromptLog(BaseModel):
    user_role: str
    prompt: str
    response: str

class PromptLogOut(PromptLog):
    timestamp: datetime

    class Config:
        orm_mode = True
