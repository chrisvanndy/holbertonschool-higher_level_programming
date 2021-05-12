#!/usr/bin/python3
"""Module creates method from_json_string() which converts JSON string into\
a ptython ojbect using the loads() function"""


import json


def from_json_string(my_str):
    """from_json_string imports "my_str" and converts JSON str to PY obj"""

    theObj = json.loads(my_str)
    return theObj
