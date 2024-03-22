#!/usr/bin/python3

"""
Connects to MySQL, adds the State object "Louisiana" to
the specified database.

Returns:
    None. Prints the id of the newly created State object
    to the console.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def add_state(username, password, database):
    """
    Connects to MySQL, adds the State object "Louisiana" to
    the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the MySQL database containing
        the State objects.

    Returns:
        None. Prints the id of the newly created State object
        to the console.
    """

    engine = create_engine(
        f'mysql://{username}:{password}@localhost:3306/{database}')

    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    new_state = State(name="Louisiana")

    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    add_state(username, password, database)
