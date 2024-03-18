#!/usr/bin/python3

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def change_state_name(username, password, database):
    """
    Connects to MySQL, changes the name of a State object in the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the MySQL database containing the State objects.

    Returns:
        None. Prints a message indicating success or failure.
    """
    # Create engine to connect to MySQL server
    engine = create_engine(f'mysql://{username}:{password}@localhost:3306/{database}')

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Query the State object with id = 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # Update the name of the State object if found
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()
        print("Name changed successfully.")
    else:
        print("State with id = 2 not found.")

    # Close session
    session.close()

if __name__ == "__main__":
    # Extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the change_state_name function with provided arguments
    change_state_name(username, password, database)
