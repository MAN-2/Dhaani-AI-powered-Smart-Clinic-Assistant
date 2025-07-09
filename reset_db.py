# init_db.py

from sqlalchemy import text
from app.database import engine, Base

# 🔧 This import must execute Doctor & Appointment definitions
import app.ormmode  # Doctor and Appointment must live here

print("🔗 Connected to:", engine.url)

# 🧹 Drop existing tables safely
with engine.connect() as conn:
    conn.execute(text("DROP TABLE IF EXISTS appointments CASCADE"))
    conn.execute(text("DROP TABLE IF EXISTS doctors CASCADE"))

# 🚀 Register tables from Base.metadata
Base.metadata.create_all(bind=engine)
print("✅ Tables created successfully.")
