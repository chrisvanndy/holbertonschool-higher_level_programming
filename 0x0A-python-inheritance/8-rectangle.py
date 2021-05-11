#!/usr/bin/python3
"""Define BaseGeometry, an empty class"""


class BaseGeometry():
    """ BaseGeometry is the super() class """

    def area(self):
        """Returns the area of a shape"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value passed to method"""
        if not isinstance(value, int) or type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Rectangle is a child class of BaseGeometry """

    def __init__(self, width, height):
        """ initializes values for height and width if passed validator """
        if BaseGeometry.integer_validator(self, "width", width):
            self.__width = width
        if BaseGeometry.integer_validator(self, "height", height):
            self.__height = height
