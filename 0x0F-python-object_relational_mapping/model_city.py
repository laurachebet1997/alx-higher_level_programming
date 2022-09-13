#!/usr/bin/python3
'''contains a class City
'''

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeingnKey
from model_state import Base, State


class City(Base):
    '''Representing a class City'''

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
