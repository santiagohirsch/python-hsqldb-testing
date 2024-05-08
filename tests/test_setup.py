import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app import Base, SessionLocal, Engine

@pytest.fixture(scope="module")
def setup_database():
    print("\nSetting up database")
    Base.metadata.create_all(bind=Engine)
    yield SessionLocal()
    print("\n\n\nTearing down database")
    Base.metadata.drop_all(bind=Engine)

@pytest.fixture(scope="function")
def setup_function():
    engine = Engine
    print("\n\n\nSetting up function")
    with engine.connect() as conn:
        with conn.begin():
            with open("resources/test_inserts.sql", "r") as f:
                create_table_sql = f.read()
            conn.execute(text(create_table_sql))
    yield
    print("\nTearing down function")
    with engine.connect() as conn:
        with conn.begin():
            with open("resources/test_teardown.sql", "r") as f:
                create_table_sql = f.read()
            conn.execute(text(create_table_sql))
