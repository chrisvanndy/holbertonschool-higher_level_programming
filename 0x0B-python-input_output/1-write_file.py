#!/usr/bin/python3
""" Module contains method write_file. which writes to a file,
    and returns number of chars written"""


def write_file(filename="", text=""):
    """ writes text to a file, and returns number of chars written """
    with open(filename, 'w+', encoding='utf-8') as theFile:
        charswritten = theFile.write(text)
    return (charswritten)
