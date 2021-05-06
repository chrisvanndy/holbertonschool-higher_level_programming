#!/usr/bin/python3
""" Class Square has instantiated variable size, @property decorator
    to return size, @size.setter to set size if errors dont arise
    and an area function to determine area of a "square"
    """


class Square:
    """ Square contains perameters which define the class type square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """ size() is a getter function
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ size(self, value) is the setter function with perameters
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ position() is a getter function
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ position(self, value) is the setter function for position()
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if min(value) < 0:
            self.__position = (0, 0)
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Returns the area of class type square
        """
        area = self.size ** 2
        return area

    def my_print(self):
        """ Prints the square using area() with # character
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                for k in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print()
