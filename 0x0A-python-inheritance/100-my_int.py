#!/usr/bin/python3
""" This module will define a class and invert returns"""


class MyInt(int):
    """ MyInt is a rebel class, who loves opposite day"""

    def __init__(self, num):
        self.num = num

    def __eq__(self, other):
        """ handle == with magic method """
        if self.num is other:
            return False
        return not other

    def __ne__(self, other):
        """ handle != magic method"""
        if self.num < 0:
            if self.num is not other:
                return True
            else:
                return False
        if self.num is other:
            return True
        return False
