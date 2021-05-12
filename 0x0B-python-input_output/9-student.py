#!/usr/bin/python3
"""Modue creates method class_to_json() which returns the\
dictionary description as simple data structure for JSON\
serialization of an object."""

class Student:
    """class Student declared with publid instance attr\
    first_name, last_name, and age"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ to_json returns the class __dict__"""
        return self.__dict__
