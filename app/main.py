import os
from dotenv import load_dotenv
from fastapi import FastAPI


from app.database import engine, Base

# Routers
from app.agent import router as agent_router
from app.routers.doctor import router as doctor_router
from app.routers.appointment import router as appointment_router
from app.routers import test_email  
from app.routers import test_bookings
from app.orm_models import phist
env_path = os.path.join(os.path.dirname(__file__), os.pardir, ".env")
load_dotenv(dotenv_path=env_path)

# db creation
Base.metadata.create_all(bind=engine)
from fastapi.middleware.cors import CORSMiddleware
# FastAPI app
app = FastAPI(
    title="Doctor Appointment & Reporting Assistant",
    version="1.0.0",
)
#CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"] for stricter control
    allow_credentials=True,
    allow_methods=["*"],  # or ["GET", "POST"] for stricter control
    allow_headers=["*"],
)
# Health check endpoint
@app.get("/", tags=["health"])
async def read_root():
    return {"status": "up", "message": "Doctor MCP API running!"}

# Test routes
app.include_router(agent_router, prefix="/agent", tags=["agent"])
app.include_router(doctor_router, prefix="/doctors", tags=["doctors"])
app.include_router(appointment_router, prefix="/appointments", tags=["appointments"])
app.include_router(test_email.router)  

app.include_router(test_bookings.router)
