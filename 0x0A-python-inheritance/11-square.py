#!/usr/bin/python3
""" Define class Square, which inherits fromn Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square inherits from Rectangle, which inherits from BG"""

    def __init__(self, size):
        """intializing size of equal sided polygon"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area for class type Square"""
        return self.__size ** 2

    def __str__(self):
        """string for class type Square"""
        return "[Square] {}/{}".format(self.__size, self.__size)

