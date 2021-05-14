#!/usr/bin/python3
"""new class Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y,  id)
        self.size = size

    def __str__(self):
        sqr = "[Square] ({}) {}".format(self.id, self.x)
        sqr += "/{} - {}".format(self.y, self.size)
        return sqr

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value
