#!/usr/bin/python3
"""Module creates method load_from_json_file which writes a function\
that creates an object from a .json file"""


import json


def load_from_json_file(filename):
    """load_from_json_file creates an object from a JSON file"""
    with open(filename, 'r') as jFile:
        fString = jFile.read()
        fObj = json.loads(fString)
    return fObj
