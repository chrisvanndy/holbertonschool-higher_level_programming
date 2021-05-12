#!/usr/bin/python3
""" read_file opens a file and prints to stdout """


def read_file(filename=""):
    """ read_file opens "filename" passed from main and prints """
    with open(filename, mode="r", encoding="utf-8") as text:
        print(text.read(), end="")
