# init_db.py
from app.database import engine, Base
import app.ormmode        # registers Doctor & Appointment

# drop old tables
Base.metadata.drop_all(bind=engine)

# make brand-new ones
Base.metadata.create_all(bind=engine)

print("Tables dropped & re-created in doctor_ai")
