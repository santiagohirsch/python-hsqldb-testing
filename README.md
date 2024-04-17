# python-hsqldb-testing

This repository contains an example of in-memory HSQLDB testing.

## Introduction

This repository is built with [Python](https://www.python.org/) and uses [SQLAlchemy](https://www.sqlalchemy.org/) and [Pytest](https://docs.pytest.org/en/8.0.x/index.html)

### Project structure

The project structure is the following:

    ```
    .
    ├── Makefile
    ├── README.md
    ├── __init__.py
    ├── app.py
    └── src
        ├── __init__.py
        ├── models
        │   ├── __init__.py
        │   └── user.py
        ├── persistence
        │   ├── __init__.py
        │   └── user_dao.py
        ├── schemas
        │   ├── __init__.py
        │   └── user_schema.py
        └── tests
            ├── __init__.py
            ├── test_setup.py
            └── user_dao_test.py
    ```

### Running the tests

In order to run the tests execute the following command:

    ```sh
    make run_tests
    ```

### Clean

In order to clean the project execute the following command:

    ```sh
    make clean
    ```