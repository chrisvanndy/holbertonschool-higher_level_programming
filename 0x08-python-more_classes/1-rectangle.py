#!/usr/bin/python3
""" Define Class: Rectangle"""


class Rectangle:
    """ Class Rectangle """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ width() is property of instance width """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter sets private variable based on parameters """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ height() is a property of instance height """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter sets private variable based on parameters """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
