import pytest
from sqlalchemy import text
from src.schemas.user_schema import UserCreate
from src.persistence.user_dao import create_user, get_user, update_user, delete_user
from tests.test_setup import setup_database, setup_function


@pytest.mark.parametrize(
   "email,password",
   [
       ("test@example.com", "password"),
       ("another@example.com", "12345"),
   ],
)
def test_create_user(setup_database, email, password, setup_function):
   print("\nTesting creating user")
   user_create = UserCreate(email=email, password=password)
   user = create_user(setup_database, user_create)
   assert user.email == email
   assert user.hashed_password == f"{password}notreallyhashed"

def test_get_user(setup_database, setup_function):
   print("\nTesting getting user")
   user = get_user(setup_database, user_id=1)
   assert user.id == 1
   assert user.email == "user1@example.com"
   assert user.hashed_password == "examplenotreallyhashed1"

def test_update_user(setup_database, setup_function): 
   print("\nTesting updating user")
   updated_user = update_user(setup_database, user_id=1, email="newemail@example.com", password="newpassword")
   assert updated_user.email == "newemail@example.com"
   assert updated_user.hashed_password == "newpasswordnotreallyhashed"

def test_delete_user(setup_database, setup_function):
   print("\nTesting deleting user")
   deleted_user_id = delete_user(setup_database, user_id=1)
   assert deleted_user_id == 1
