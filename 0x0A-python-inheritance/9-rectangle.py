#!/usr/bin/python3
"""Define BaseGeometry, an empty class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle is a child class of BaseGeometry """

    def __init__(self, width, height):
        """ initializes values for height and width if passed validator """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ str prints name of class and <width>/<height>"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """ area returns area of a rectangle"""
        return self.__width * self.__height
