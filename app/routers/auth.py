# app/routers/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.ormschemas.auth import UserCreate, UserRead, Token
from app.crud.auth import get_user_by_email, create_user, verify_password
from app.auth import create_access_token, get_db

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup", response_model=UserRead, status_code=201)
def signup(user_in: UserCreate, db: Session = Depends(get_db)):
    if get_user_by_email(db, user_in.email):
        raise HTTPException(400, "Email already registered")
    return create_user(db, user_in)

@router.post("/token", response_model=Token)
def login(form: OAuth2PasswordRequestForm = Depends(),
          db: Session = Depends(get_db)):
    user = get_user_by_email(db, form.username)
    if not user or not verify_password(form.password, user.hashed_password):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED,
                            "Incorrect username or password")
    token = create_access_token(sub=str(user.id))
    return {"access_token": token, "token_type": "bearer"}
