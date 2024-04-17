import pytest
from src.schemas.user_schema import UserCreate
from src.persistence.user_dao import create_user, get_user
from src.tests.test_setup import db

@pytest.mark.parametrize(
   "email,password",
   [
       ("test@example.com", "password"),
       ("another@example.com", "12345"),
   ],
)
def test_create_user(db, email, password):
   user_create = UserCreate(email=email, password=password)
   user = create_user(db, user_create)
   assert user.email == email
   assert user.hashed_password == f"{password}notreallyhashed"

@pytest.mark.parametrize(
   "email,password",
   [
       ("test2@example.com", "password"),
       ("another2@example.com", "12345"),
   ],
)
def test_get_user(db, email, password):
   user_create = UserCreate(email=email, password=password)
   created_user = create_user(db, user_create)
   retrieved_user = get_user(db, created_user.id)
   assert retrieved_user.id == created_user.id