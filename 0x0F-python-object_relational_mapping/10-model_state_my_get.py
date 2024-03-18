#!/usr/bin/python3

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def print_state_by_name(username, password, database, state_name):
    """
    Connects to MySQL, prints the State object with the specified
    name from the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the MySQL database containing
        the State objects.
        state_name (str): Name of the state to search for.

    Returns:
        None. Prints the id of the State object with the specified
        name to the console, or "Not found" if not found.
    """
    # Create engine to connect to MySQL server
    engine = create_engine(
        f'mysql://{username}:{password}@localhost:3306/{database}')

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Query State object with the specified name
    state = session.query(State).filter(State.name == state_name).first()

    # Display result
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close session
    session.close()


if __name__ == "__main__":
    # Extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Call the print_state_by_name function with provided arguments
    print_state_by_name(username, password, database, state_name)
