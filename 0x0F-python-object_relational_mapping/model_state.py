#!/usr/bin/python3
""" This model creates the class State"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):

    """Introduces State Class which inherit from Base)"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, unique=True, nullable=True)
    name = Column(String(128), nullable=False)
