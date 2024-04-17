from src.models.user import User
from src.schemas.user_schema import UserCreate
from sqlalchemy.orm import Session

def get_user(db: Session, user_id: int):
   return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserCreate):
   db_user = User(email=user.email, hashed_password=f"{user.password}notreallyhashed")
   db.add(db_user)
   db.commit()
   db.refresh(db_user)
   return db_user