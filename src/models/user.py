from app import Base
from sqlalchemy import Boolean, Column, Integer, String

class User(Base):
   __tablename__ = "user"

   id = Column(Integer, primary_key=True, index=True)
   email = Column(String, unique=True, index=True)
   hashed_password = Column(String)