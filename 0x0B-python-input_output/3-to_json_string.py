#!/usr/bin/python3
"""Module creates method to_json_string() which takes input, and returns\
the JSON representation of that object(a string)"""


import json


def to_json_string(my_obj):
    """takes my_obj, returns JSON representation (a string)"""

    jStr = json.dumps(my_obj)
    return jStr
