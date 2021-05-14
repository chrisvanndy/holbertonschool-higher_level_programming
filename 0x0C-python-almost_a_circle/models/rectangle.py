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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """__str__ method represents the class object Rectangle"""
        string = "[Rectangle] ({}) ".format(self.id)
        string += "{}/{} - {}/{}".format(self.x, self.y, self
                                         .width, self.height)
        return string

    def area(self):
        """ area is class method; returns area of rectangle"""
        return self.height * self.width

    def display(self):
        """ display is a class method; prints "Rec" to stdout"""
        for row in range(self.height):
            for column in range(self.width):
                print("#", end="")
            print()

    @property
    def width(self):
        """getter for 'width' private instance attr"""

        return self.__width

    @width.setter
    def width(self, value):
        """ Width setter function"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for 'x' private instance attr"""

        return self.__height

    @height.setter
    def height(self, value):
        """setter for 'x' private instance attr"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for 'x' private instance attr"""

        return self.__x

    @x.setter
    def x(self, value):
        """setter for 'x' private instance attr"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for 'y' private instance attr"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for 'y' private instance attr"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
