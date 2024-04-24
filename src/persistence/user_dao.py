from src.models.user import User
from src.schemas.user_schema import UserCreate
from sqlalchemy.orm import Session

def get_user(db: Session, user_id: int) -> User:
   return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserCreate) -> User:
   db_user = User(email=user.email, hashed_password=f"{user.password}notreallyhashed")
   db.add(db_user)
   db.commit()
   db.refresh(db_user)
   return db_user

def update_user(db: Session, user_id: int, email: str, password: str) -> User:
   db_user = get_user(db, user_id)
   db_user.email = email
   db_user.hashed_password = f"{password}notreallyhashed"
   db.commit()
   db.refresh(db_user)
   return db_user

def delete_user(db: Session, user_id: int) -> int:
   db_user = get_user(db, user_id)
   db.delete(db_user)
   db.commit()
   return user_id