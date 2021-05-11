#!/usr/bin/python3
""" MyList will inherit from list and return ordered list """


class MyList(list):
    """ MyList is super() class of this module """

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
