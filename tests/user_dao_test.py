import pytest
from src.schemas.user_schema import UserCreate
from src.persistence.user_dao import create_user, get_user, update_user, delete_user
from tests.test_setup import db

@pytest.mark.parametrize(
   "email,password",
   [
       ("test@example.com", "password"),
       ("another@example.com", "12345"),
   ],
)
def test_create_user(db, email, password):
   db.begin()
   user_create = UserCreate(email=email, password=password)
   user = create_user(db, user_create)
   assert user.email == email
   assert user.hashed_password == f"{password}notreallyhashed"
   db.rollback()

def test_get_user(db):
   db.begin()
   user = get_user(db, user_id=1)
   assert user.id == 1
   assert user.email == "user1@example.com"
   assert user.hashed_password == "examplenotreallyhashed1"
   db.rollback()

def test_update_user(db): 
   db.begin()
   updated_user = update_user(db, user_id=1, email="newemail@example.com", password="newpassword")
   assert updated_user.email == "newemail@example.com"
   assert updated_user.hashed_password == "newpasswordnotreallyhashed"
   db.rollback()

def test_delete_user(db):
   db.begin()
   deleted_user_id = delete_user(db, user_id=1)
   assert deleted_user_id == 1
   db.rollback()