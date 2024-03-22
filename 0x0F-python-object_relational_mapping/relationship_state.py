#!/usr/bin/python3

"""
Defines the State class using SQLAlchemy ORM to
interact with the 'states' table in a MySQL database.

This script defines a SQLAlchemy Base class and a
State class that represents the 'states' table.
The State class maps to the 'states' table and
defines its structure including columns and relationships.

Attributes:
    Base: The declarative base class provided by
    SQLAlchemy for defining
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        cascade="all, delete",
        back_populates="state")
