#!/usr/bin/python3
"""Contains a class City"""
from sqlalchemy import Column, Integer, String, ForeingnKey
from model_state import Base, State


class City(Base):
     """Represents a city for a MySQL database.
     Attributes:
     id (str): The city's id.
     name (sqlalchemy.Integer): The city's name.
     state_id (sqlalchemy.String): The city's state id.
     """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
