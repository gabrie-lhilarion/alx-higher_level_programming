#!/usr/bin/python3

"""
Connects to MySQL, fetches and prints all City objects
from the specified database.


Returns:
    None. Prints the City objects to the console.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def fetch_cities_by_state(username, password, database):
    """
    Connects to MySQL, fetches and prints all City objects
    from the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the MySQL database containing
        the City objects.

    Returns:
        None. Prints the City objects to the console.
    """

    engine = create_engine(
        f'mysql://{username}:{password}@localhost:3306/{database}')

    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        state_name = session.query(
            State.name).filter(
            State.id == city.state_id).scalar()
        print(f"{state_name}: ({city.id}) {city.name}")

    session.close()


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    fetch_cities_by_state(username, password, database)
