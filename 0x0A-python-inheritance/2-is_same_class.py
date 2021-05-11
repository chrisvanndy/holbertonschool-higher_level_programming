#!/usr/bin/python3
""" is_same_class takes an object and class and returns True or False"""


def is_same_class(obj, a_class):
    """ is_same_classe returns true or false based on instance of object
    """
    if isinstance(obj, a_class) and type(obj) == a_class:
        return True
    else:
        return False
