#!/usr/bin/python3

"""
Connects to MySQL, prints the State object with the specified
name from the specified database.

Returns:
    None. Prints the id of the State object with the specified
    name to the console, or "Not found" if not found.
"""

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

    engine = create_engine(
        f'mysql://{username}:{password}@localhost:3306/{database}')

    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    print_state_by_name(username, password, database, state_name)
