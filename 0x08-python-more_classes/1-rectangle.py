#!/usr/bin/python3
""" Define Class: Rectangle"""


class Rectangle:
    """ Class Rectangle """
    __width = 0
    __height = 0
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width() is property of instance width """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter sets private variable based on parameters """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")    
        else:
            self.__width = value
    
    @property
    def height(self):
        """ height() is a property of instance height """
        return self.__height
    
    @height.setter
    def height(self, value):
        """ height setter sets private variable based on parameters """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer") 
        else:
            self.__height = value
