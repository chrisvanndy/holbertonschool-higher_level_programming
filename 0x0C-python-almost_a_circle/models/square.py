#!/usr/bin/python3
"""new class Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y,  id)

    def __str__(self):
        sqr = "[Square] {} {}".format(self.id, self.x)
        sqr += "/{} = {}".format(self.y, self.width)
        return sqr
