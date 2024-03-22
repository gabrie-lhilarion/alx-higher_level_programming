#!/usr/bin/python3

"""
Defines the City class using SQLAlchemy ORM to interact
with the 'cities' table in a MySQL database.

This script defines a City class that represents the
'cities' table and its relationships.
The City class maps to the 'cities' table and defines
its structure including columns and relationships.

Attributes:
    Base: The declarative base class provided by SQLAlchemy
    for defining database models.
    City: A class representing the 'cities' table in the
    database. It includes columns for 'id', 'name',
    'state_id' (foreign key), and a relationship
    with the State class representing the state
    associated with each city.

Classes:
    City: Represents a city in the 'cities' table with
    columns for 'id', 'name', and 'state_id'.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    """
    Represents a city in the 'cities' table.

    Attributes:
        id (int): Primary key for the city, auto-incremented.
        name (str): Name of the city.
        state_id (int): Foreign key referencing the id of the
        state associated with this city.
        state (relationship): Relationship with the State class
        epresenting the state associated with this city.
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")
