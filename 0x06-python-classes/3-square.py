#!/usr/bin/python3
""" Square class gets private variable size, checks to raise errors
    before setting the value of the variable, and a method to determine
    area of a "square" """


class Square:
    """ Square contains perameters which define the class type square
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Returns the area of class type square
        """
        area = self.__size ** 2
        return area
