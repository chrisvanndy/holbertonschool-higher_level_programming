#!/usr/bin/python3
"""Define class Base: and its attribute __nb_objects"""

import json


class Base:
    """Base is a class which will be expanded in future tasks"""
    # private class attribute nb_objects is incrementation var
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string converts dicts to json string"""
        json_str = []
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return json_str
        json_str = json.dumps(list_dictionaries)
        return json_str
