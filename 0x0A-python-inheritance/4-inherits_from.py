#!/usr/bin/python3
""" inherits_from takes an object and class and returns True or False"""


def inherits_from(obj, a_class):
    """inherits_from returns T or F based on type and class"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
