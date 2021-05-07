#!/usr/bin/python3
""" Module add_integer tests for appropriate vaules being passed / adds """


def add_integer(a, b=98):
    """ add_integer function receives values and adds
    """
    # determine a and be are int or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # handle float values
    if a == float('inf'):
        raise TypeError("a must be an integer")
    if b == float('inf'):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
