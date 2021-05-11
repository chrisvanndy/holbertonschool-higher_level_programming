#!/usr/bin/python3
""" Define class Square, which inherits fromn Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square inherits from Rectangle, which inherits from BG"""

    def __init__(self, size):
        """intializing size of equal sided polygon"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area for class type Square"""
        return self.__size ** 2
