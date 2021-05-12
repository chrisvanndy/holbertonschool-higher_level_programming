#!/usr/bin/python3
"""Modue creates method class_to_json() which returns the\
dictionary description as simple data structure for JSON\
serialization of an object."""


def class_to_json(obj):
    """class_to_json returns dict description"""

    return obj.__dict__
