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

    @classmethod
    def create(cls, **dictionary):
        """create will retun an instance obj with attributes set"""
        if isinstance(cls, Square):
            dummy = Square(1)
            dummy.update(**dictionary)
        else:
            dummy = Rectangle(1, 1)
            dummy.update(**dictionary)
        return dummy

    # will reaquire cls instead of self
    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file writes the json rep str "list_objs" to a file"""
        new_file = cls.__name__ + ".json"
        the_list = []
        if list_objs:
            for objects in list_objs:
                dict_obj = cls.to_dictionary(objects)
                the_list.append(dict_obj)
                # now a list of dictionaries exits ^^ to pass to to_json_string
            json_str = cls.to_json_string(the_list)
        else:
            json_str = "[]"
        with open(new_file, 'w') as new:
            new.write(json_str)

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string converts dicts to json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        json_str = json.dumps(list_dictionaries)
        return json_str

    @staticmethod
    def from_json_string(json_string):
        """from_json_string returns a list from the json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        new_list = json.loads(json_string)
        return new_list
