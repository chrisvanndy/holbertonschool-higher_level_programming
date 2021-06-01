#!/usr/bin/python3
""" This model creates the class City"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import State

Base = declarative_base()


class City(Base):
    """ Introduces City class which inherits from Base"""
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
