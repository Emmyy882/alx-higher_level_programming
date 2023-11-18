#!/usr/bin/python3
"""
Contains the class definition of a State and an instance \
        Base = declarative()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()
"""Represents the base class for all tables"""


class State(Base):
    """A class that inherits from Base"""

    # Creating a table 'states'
    __tablename__ = 'states'

    id = Column(Integer,
            autoincrement=True,
            unique=True,
            nullable=False,
            primary_key=True
            )
    name = Column(
            String(128),
            nullable=False
            )
