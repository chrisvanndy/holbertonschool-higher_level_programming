#!/usr/bin/python3
"""new class Square"""


from models.rectangle import Rectangle
import inspect


class Square(Rectangle):
    """Class square inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y,  id)
        self.size = size

    def __str__(self):
        sqr = "[Square] ({}) {}".format(self.id, self.x)
        sqr += "/{} - {}".format(self.y, self.size)
        return sqr

    def to_dictionary(self):
        """to_dictionary reutrns the dictionary representation of Square"""
        sqr_dict = {}
        for i in inspect.getmembers(self):
            if not i[0].startswith("_"):
                if not inspect.ismethod(i[1]) and\
                   not inspect.isfunction(i[1]):
                    if i[0] == "width" or i[0] == "height":
                        continue
                    sqr_dict[i[0]] = i[1]
        return sqr_dict

    def update(self, *args, **kwargs):
        """ update resets values for Rectangle"""
        # *args is a tuple, typecast(args) to a new list
        if args is None or len(args) == 0:
            for i in kwargs:
                if hasattr(self, i):
                    setattr(self, i, kwargs[i])
        else:
            largs = list(args)
            kwlargs = ["id", "size", "x", "y"]
            for i in range(len(largs)):
                setattr(self, kwlargs[i], largs[i])

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
