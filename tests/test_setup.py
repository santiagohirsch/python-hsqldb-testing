import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app import Base

@pytest.fixture(scope="module")
def db():
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})

    # Create session
    TestSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    session = TestSession()

    # Execute SQL script to create and populate test data
    with engine.connect() as conn:
        with conn.begin():
            with open("resources/test_table.sql", "r") as f:
                create_table_sql = f.read()
            conn.execute(text(create_table_sql))
            with open("resources/test_inserts.sql", "r") as f:
                insert_data_sql = f.read()
            conn.execute(text(insert_data_sql))



    yield session
    session.close()

@pytest.fixture(scope="module", autouse=True)
def cleanup(request, db):
    yield
    db.close()
