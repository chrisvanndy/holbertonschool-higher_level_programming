#!/usr/bin/python3
""" say_my_name will print "My name is <first name><last name>" """


def say_my_name(first_name, last_name=""):
    """ say_my_name confirms that first and last name are strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
