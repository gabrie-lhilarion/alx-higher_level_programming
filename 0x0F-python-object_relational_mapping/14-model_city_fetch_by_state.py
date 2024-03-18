#!/usr/bin/python3

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
    # Create engine to connect to MySQL server
    engine = create_engine(
        f'mysql://{username}:{password}@localhost:3306/{database}')

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Query all City objects and sort by id
    cities = session.query(City).order_by(City.id).all()

    # Display results
    for city in cities:
        state_name = session.query(
            State.name).filter(
            State.id == city.state_id).scalar()
        print(f"{state_name}: ({city.id}) {city.name}")

    # Close session
    session.close()


if __name__ == "__main__":
    # Extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the fetch_cities_by_state function with provided arguments
    fetch_cities_by_state(username, password, database)
