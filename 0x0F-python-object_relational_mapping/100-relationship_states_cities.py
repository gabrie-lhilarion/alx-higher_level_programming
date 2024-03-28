#!/usr/bin/python3

"""
Connects to MySQL, creates the State "California" with
the City "San Francisco" in the specified database.

Returns:
    None.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def create_state_and_city(username, password, database):
    """
    Connects to MySQL, creates the State "California" with
    the City "San Francisco" in the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the MySQL database to create
        the State and City objects.

    Returns:
        None.
    """

    engine = create_engine(
        f'mysql://{username}:{password}@localhost:3306/{database}')

    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    california = State(name="California")

    san_francisco = City(name="San Francisco", state=california)

    session.add(california)
    session.add(san_francisco)
    session.commit()

    session.close()


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    create_state_and_city(username, password, database)
