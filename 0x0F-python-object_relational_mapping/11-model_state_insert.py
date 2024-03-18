#!/usr/bin/python3

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def add_state(username, password, database):
    """
    Connects to MySQL, adds the State object "Louisiana" to the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the MySQL database containing the State objects.

    Returns:
        None. Prints the id of the newly created State object to the console.
    """
    # Create engine to connect to MySQL server
    engine = create_engine(f'mysql://{username}:{password}@localhost:3306/{database}')

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Create a new State object
    new_state = State(name="Louisiana")

    # Add the new State object to the session and commit changes
    session.add(new_state)
    session.commit()

    # Print the id of the newly created State object
    print(new_state.id)

    # Close session
    session.close()

if __name__ == "__main__":
    # Extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the add_state function with provided arguments
    add_state(username, password, database)
