from core.security import get_password_hash
from domain.models.user import User
from infrastructure.db import SessionLocal
from schemas.user import UserCreate


def create_user(user: UserCreate):
    db = SessionLocal()
    db_user = User(username=user.username, hashed_password=get_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
