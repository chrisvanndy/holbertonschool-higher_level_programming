#!/usr/bin/python3
""" Module add_integer tests for appropriate vaules being passed / adds """


def add_integer(a, b=98):
    """ add_integer function receives values and adds
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
