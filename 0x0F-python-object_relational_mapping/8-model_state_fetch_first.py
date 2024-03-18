#!/usr/bin/python3

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def print_first_state(username, password, database):
    """
    Connects to MySQL, prints the first State object
    from the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the MySQL database
        containing the State objects.

    Returns:
        None. Prints the first State object to the
        console.
    """
    # Create engine to connect to MySQL server
    engine = create_engine(
        f'mysql://{username}:{password}@localhost:3306/{database}')

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Query the first State object
    first_state = session.query(State).order_by(State.id).first()

    # Display result
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close session
    session.close()


if __name__ == "__main__":
    # Extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the print_first_state function with provided arguments
    print_first_state(username, password, database)
