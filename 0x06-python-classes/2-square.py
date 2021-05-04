#!/usr/bin/python3
""" Square gets private variable size instantiated with value 0 """


class Square:
    """ Square class type initializes with variable size to 0
    value checks are implemented to raise errors before setting
    the value of the variable """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
