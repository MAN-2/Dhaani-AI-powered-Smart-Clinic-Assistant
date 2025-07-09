# MCP AGENT AND HISTORY Configurations

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from app.database import get_db
from app.orm_models.phist import PromptHistory
from app.orm_schemas.phist import PromptLogOut
from app.mcp.agentm import run_agent

from app.orm_schemas.doctor import DoctorCreate, DoctorRead
from app.orm_schemas.appointment import AppointmentCreate, AppointmentRead

router = APIRouter()

class AgentInput(BaseModel):
    user_input: str

@router.post("/mcp-agent")
def mcp_agent(input: AgentInput, db: Session = Depends(get_db)):
    try:
        result = run_agent(input.user_input, db)

        log = PromptHistory(
            user_role="patient",  # Or detect from prompt/headers
            prompt=input.user_input,
            response=result["message"]
        )

        db.add(log)
        db.commit()

        return result
    except Exception as e:
        import traceback
        print("Error in route")
        traceback.print_exc()
        return {"error":str(e)}
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/history", response_model=List[PromptLogOut])
def get_prompt_history(db: Session = Depends(get_db)):
    return db.query(PromptHistory).order_by(PromptHistory.timestamp.desc()).all()
