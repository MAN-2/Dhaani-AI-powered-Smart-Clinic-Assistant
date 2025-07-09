

import json
import os
import requests
from typing import Dict, Any
from dotenv import load_dotenv
from sqlalchemy.orm import Session

from app.mcp.tools import (
    check_doctor_availability,
    AvailabilityInput,
    reschedule_appointment,
    RescheduleInput,
    book_appointment,
    BookAppointmentInput,
    send_confirmation_email,     
)
from  app.mcp.tools import generate_summary_report
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY") # Set in env file 

TOOLS = {  #TOOLS DEFINITION
    "check_doctor_availability": {
        "function": check_doctor_availability,
        "input_schema": AvailabilityInput,
        "description": "Get a doctor's available time slots for a specific date"
    },
    "reschedule_appointment": {
        "function": reschedule_appointment,
        "input_schema": RescheduleInput,
        "description": "Reschedule a booked appointment by ID"
    },
    "book_appointment": {
        "function": book_appointment,
        "input_schema": BookAppointmentInput,
        "description": "Book a doctor appointment. Requires: doctor_name, patient_email, reason, date (YYYY-MM-DD), time (HH:MM)"
    },
    "send_confirmation_email": {     
        "function": send_confirmation_email,
        "input_schema": None,
        "description": "Send appointment confirmation email to patient"
    },
    


    "generate_summary_report": {
        "function": generate_summary_report,
        "input_schema": None,  # No Pydantic
        "description": "Generates a visit summary report for a doctor over a date range or all dates"
}

       }
    





def construct_prompt(goal: str) -> str:
    tool_descriptions = "\n".join([
        f"- {name}: {tool['description']} | Params: {tool['input_schema'].__annotations__ if tool['input_schema'] else 'custom JSON'}"
        for name, tool in TOOLS.items()
    ])
    return f"""
You are a smart doctor assistant LLM agent that calls tools via JSON.
ASSUME: The doctor currently using this system has doctor_id = 1. 
TOOLS:
{tool_descriptions} 

User says:
{goal}

Return ONLY this JSON (no markdown):

{{
  "action": "<tool_name>",
  "params": {{}},
  "message": ""
}}

⚠️ RULES:
- Use valid types for each tool’s params.
- Respond with valid data only.
"""

#doctor_id=1 is added to handle agent error of id 

def call_llm(prompt: str) -> Dict[str, Any]:
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "http://localhost",
        "X-Title": "doctor-agent",
    }

    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": "You are a helpful doctor assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=payload
    )
    result = response.json()
    return json.loads(result["choices"][0]["message"]["content"])


# === MAIN ENTRY POINT ===
def run_agent(user_input: str, db: Session) -> Dict[str, Any]:
    prompt = construct_prompt(user_input)
    parsed = call_llm(prompt)

    action = parsed.get("action")
    params = parsed.get("params", {})
    # Inject fallback 
    if action == "generate_summary_report" and "doctor_id" not in params:
    
        params["doctor_id"] = "b61245da-6d7f-4fc2-b456-c83d88fbe98a" 

    message = parsed.get("message", "")
    tool_result = None

    if action not in TOOLS:
        return {"error": f"Unknown tool: {action}"}

    tool = TOOLS[action]
    input_schema = tool["input_schema"]
    tool_func = tool["function"]

    if "appointment_id" in params and isinstance(params["appointment_id"], str):
        try:
            params["appointment_id"] = int(params["appointment_id"])
        except:
            raise ValueError("appointment_id must be an integer")

    if input_schema:
        validated = input_schema(**params)
        tool_result = tool_func(validated, db=db)
    else:
        try:
            print("🧪 Calling tool with params:", params)

            tool_result = tool_func(**params, db=db)
        except Exception as e:
            raise RuntimeError(f"❌ Tool execution failed: {e}")

    return {
        "message": message,
        "tool_used": action,
        "tool_result": tool_result
    }
