#!/usr/bin/python3
""" Documentation for module print_square"""


def print_square(size):
    """ print_square handles printing of square under certain conditions """
    if isinstance(size, int):
        if size < 0:
            raise ValueError("size must be >=0")
        if isinstance(size, float):
            if size < 0:
                raise ValueError("size must be an integer")
    else:
        raise TypeError("size must be an integer")

    for row in range(size):
        for row in range(size):
            print("#", end='')
        print()
