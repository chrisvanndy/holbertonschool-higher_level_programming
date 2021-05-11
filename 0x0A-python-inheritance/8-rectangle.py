#!/usr/bin/python3
"""Define BaseGeometry, an empty class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle is a child class of BaseGeometry """

    def __init__(self, width, height):
        """ initializes values for height and width if passed validator """
        super().__init__()
        if BaseGeometry.integer_validator(self, "width", width):
            self.__width = width
        if BaseGeometry.integer_validator(self, "height", height):
            self.__height = height
