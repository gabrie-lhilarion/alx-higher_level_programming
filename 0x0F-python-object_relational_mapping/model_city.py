"""
This script defines the City class, representing a city in the
MySQL database.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    Represents a city in the MySQL table cities.

    Attributes:
        id (int): An auto-generated, unique integer representing
        the city's ID.
        name (str): A string representing the name of the city.
        state_id (int): An integer representing the ID of the
        state to which the city belongs.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
