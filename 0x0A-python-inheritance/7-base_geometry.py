#!/usr/bin/python3
"""Define BaseGeometry, an empty class"""


class BaseGeometry():
    """ BaseGeometry is the super() class """
    pass

    def area(self, height, width):
        """Returns the area of a shape"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value passed to method"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
