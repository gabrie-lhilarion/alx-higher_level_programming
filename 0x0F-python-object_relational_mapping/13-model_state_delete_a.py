#!/usr/bin/python3

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states_with_letter_a(username, password, database):
    """
    Connects to MySQL, deletes all State objects with a name containing
    the letter 'a' from the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the MySQL database containing the
        State objects.

    Returns:
        None. Prints a message indicating the number of deleted records.
    """
    # Create engine to connect to MySQL server
    engine = create_engine(
        f'mysql://{username}:{password}@localhost:3306/{database}')

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Query State objects with a name containing the letter 'a'
    states_to_delete = session.query(
        State).filter(State.name.like('%a%')).all()

    # Delete the queried State objects
    if states_to_delete:
        for state in states_to_delete:
            session.delete(state)
        session.commit()
        print(f"{len(states_to_delete)} State objects deleted successfully.")
    else:
        print("No State objects found with a name containing the letter 'a'.")

    # Close session
    session.close()


if __name__ == "__main__":
    # Extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the delete_states_with_letter_a function with provided arguments
    delete_states_with_letter_a(username, password, database)
