#!/usr/bin/python3
""" is_kind_of_class takes an object and class and returns True or False"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class returns T or F based on type and class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
