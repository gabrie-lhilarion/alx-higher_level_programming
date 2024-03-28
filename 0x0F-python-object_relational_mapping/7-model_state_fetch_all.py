#!/usr/bin/python3

"""
Connects to MySQL, lists all State objects from the
specified database.

Returns:
    None. Prints the list of State objects to the console.
"""

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

    engine = create_engine(
        f'mysql://{username}:{password}@localhost:3306/{database}')

    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
