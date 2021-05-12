#!/usr/bin/python3
""" This module creates append_write, a method that creates a file
    and appends to the file when the method is called."""


def append_write(filename="", text=""):
    """append_write creates a new file, appends text when called\
    and returns the number of characters written"""

    with open(filename, 'a+', encoding='utf-8') as theFile:
        charswritten = theFile.write(text)
    return charswritten
