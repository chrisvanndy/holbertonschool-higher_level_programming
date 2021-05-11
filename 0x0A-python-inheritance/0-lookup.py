#!/usr/bin/python3
""" 0-lookup returns a list object of available attributes
    and methods of an object"""


def lookup(obj):
    """ lookup method returns a string
    """
    return(dir(obj))    
