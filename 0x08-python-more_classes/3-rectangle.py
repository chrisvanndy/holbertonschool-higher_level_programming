#!/usr/bin/python3
""" Define Class: Rectangle"""


class Rectangle:
    """ Class Rectangle """

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.width = width
        self.height = height

    def __str__(self):
        string = ""
        for i in range(self.height):
            for j in range(self.width):
                string += "#"
            if i < self.height - 1:
                string += "\n"
        return "".format(end="").join(string)

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

    def perimeter(self):
        """ perimeter is a public method returns perimeter of Rectangle """
        if self.width == 0 or self.height == 0:
            return "0"
        perimeter = ((self.__height * 2) + (self.__width * 2))
        return perimeter

    def area(self):
        """ area is a public method returns area of a Rectangle """
        area = self.__height * self.__width
        return area
