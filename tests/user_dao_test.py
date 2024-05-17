import pytest
from sqlalchemy import text
from src.schemas.user_schema import UserCreate
from src.persistence.user_dao import create_user, get_user, update_user, delete_user, count_users, count_users_where_email
from tests.test_setup import setup_database, setup_function

# DEFAULT DATABASE SETUP
# INSERT INTO user (id, email, hashed_password)
# VALUES
#     (1, 'user1@example.com', 'examplenotreallyhashed1'),
#     (2, 'user2@example.com', 'examplenotreallyhashed2'),
#     (3, 'user3@example.com', 'examplenotreallyhashed3');


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
   assert count_users(setup_database) == 4
   assert count_users_where_email(setup_database, email) == 1

def test_get_user(setup_database, setup_function):
   print("\nTesting getting user")
   user = get_user(setup_database, user_id=1)
   assert user.id == 1
   assert user.email == "user1@example.com"
   assert user.hashed_password == "examplenotreallyhashed1"
   assert count_users(setup_database) == 3
   assert count_users_where_email(setup_database, "user1@example.com") == 1

def test_update_user(setup_database, setup_function): 
   print("\nTesting updating user")
   new_email = "newemail@example.com"
   new_password = "newpassword"
   updated_user = update_user(setup_database, user_id=1, email=new_email, password=new_password)
   assert updated_user.email == new_email
   assert updated_user.hashed_password == new_password + "notreallyhashed"
   assert count_users(setup_database) == 3
   assert count_users_where_email(setup_database, new_email) == 1


def test_delete_user(setup_database, setup_function):
   print("\nTesting deleting user")
   deleted_user_id = delete_user(setup_database, user_id=1)
   assert deleted_user_id == 1
   assert count_users(setup_database) == 2
   assert count_users_where_email(setup_database, "user1@example.com") == 0
