#!/usr/bin/python3

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
    # Create engine to connect to MySQL server
    engine = create_engine(
        f'mysql://{username}:{password}@localhost:3306/{database}')

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Create State object "California"
    california = State(name="California")

    # Create City object "San Francisco" linked to "California"
    san_francisco = City(name="San Francisco", state=california)

    # Add State and City objects to session and commit changes
    session.add(california)
    session.add(san_francisco)
    session.commit()

    # Close session
    session.close()


if __name__ == "__main__":
    # Extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the create_state_and_city function with provided arguments
    create_state_and_city(username, password, database)
