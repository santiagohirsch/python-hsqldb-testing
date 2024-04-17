from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import Base
import pytest


@pytest.fixture
def db():
   engine = create_engine(
       "sqlite:///:memory:", connect_args={"check_same_thread": False}
   )
   TestSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
   Base.metadata.create_all(bind=engine)
   return TestSession()