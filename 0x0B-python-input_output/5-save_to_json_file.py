#!/usr/bin/python3
"""Module creates method save_to_json_file, which takes python object\
converts it to a json string and saves the json string in a .json file"""


import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file creates a new file, and stores passed python\
    object as a json string"""

    with open(filename, 'w') as jFile:
        jFile.write(json.dumps(my_obj))
