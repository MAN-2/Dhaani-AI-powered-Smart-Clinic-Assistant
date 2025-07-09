from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
Base = declarative_base()

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))


DATABASE_URL = os.getenv("DATABASE_URL") # Db url stored in env


engine = create_engine(DATABASE_URL)# create SQLalchemy engine


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
