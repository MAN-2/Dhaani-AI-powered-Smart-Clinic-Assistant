# app/auth.py
import os
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.crud.auth import get_user_by_email, verify_password
from app.database import SessionLocal
from app.ormschemas.auth import TokenData

SECRET_KEY = os.getenv("JWT_SECRET", "change_me")
ALGORITHM = "HS256"
ACCESS_EXPIRE_MIN = 60

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

def get_db():
    db = SessionLocal(); 
    try: yield db
    finally: db.close()

def create_access_token(sub: str):
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_EXPIRE_MIN)
    to_encode = {"exp": expire, "sub": sub}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme),
                     db: Session = Depends(get_db)):
    creds_exc = HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Invalid credentials",
      headers={"WWW-Authenticate":"Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None: raise creds_exc
    except JWTError:
        raise creds_exc
    user = db.get(get_user_by_email.__self__, user_id)  # workaround: db.get(User, user_id)
    if not user: raise creds_exc
    return user
