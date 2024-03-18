#!/usr/bin/python3

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def list_states_with_letter_a(username, password, database):
    """
    Connects to MySQL, lists all State objects containing the letter 'a' from the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the MySQL database containing the State objects.

    Returns:
        None. Prints the list of State objects containing the letter 'a' to the console.
    """
    # Create engine to connect to MySQL server
    engine = create_engine(f'mysql://{username}:{password}@localhost:3306/{database}')

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Query State objects containing the letter 'a' and sort by id
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Display results
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()

if __name__ == "__main__":
    # Extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the list_states_with_letter_a function with provided arguments
    list_states_with_letter_a(username, password, database)
