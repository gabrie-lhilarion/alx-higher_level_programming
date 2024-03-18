#!/usr/bin/python3

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(username, password, database):
    """
    Connects to MySQL, lists all State objects from the
    specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the MySQL database
        containing the State objects.

    Returns:
        None. Prints the list of State objects to the console.
    """
    # Create engine to connect to MySQL server
    engine = create_engine(
        f'mysql://{username}:{password}@localhost:3306/{database}')

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Query all State objects and sort by id
    states = session.query(State).order_by(State.id).all()

    # Display results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()


if __name__ == "__main__":
    # Extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the list_states function with provided arguments
    list_states(username, password, database)
