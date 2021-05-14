#!/usr/bin/python3
"""class Rectangle inherits from class Base, import module for\
" models/base.py and give Rectangle(Base) properties """


from models.base import Base


class Rectangle(Base):
    """ Rectangle is a subclass of Base and inherits all\
    of it's properties"""

    def __init__(self, width, height, x=0, y=0, id=None):
        # instantiate private instance attributes
        # width, height, x and y
        # call the super class with id
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def x(self):
        """getter for 'x' private instance attr"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for 'x' private instance attr"""
        self.__x = value

    @property
    def y(self):
        """getter for 'x' private instance attr"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for 'x' private instance attr"""
        self.__y = value

    @property
    def width(self):
        """getter for 'x' private instance attr"""
        return self.__width

    @width.setter
    def width(self, x):
        """setter for 'x' private instance attr"""
        self.__width = x

    @property
    def height(self):
        """getter for 'x' private instance attr"""
        return self.__height

    @height.setter
    def height(self, y):
        """setter for 'x' private instance attr"""
        self.__x = y
