
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.ormmode import User

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user_in) -> User:
    hashed = pwd_ctx.hash(user_in.password)
    user = User(email=user_in.email, hashed_password=hashed, role=user_in.role)
    db.add(user); db.commit(); db.refresh(user)
    return user

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_ctx.verify(plain, hashed)
