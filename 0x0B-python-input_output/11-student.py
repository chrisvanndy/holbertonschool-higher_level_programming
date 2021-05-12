#!/usr/bin/python3
"""Modue creates method class_to_json() which returns the\
dictionary description as simple data structure for JSON\
serialization of an object."""


class Student:
    """class Student declared with publid instance attr\
    first_name, last_name, and age"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ to_json returns the class __dict__.  First we check\
        to see if "attrs" is a list.  Then we loop throug the list\
        and confirm that Student hasattr in index of attrs.  After\
        we confirm a match, we can getattr from self if it was given\
        to us via attrs. return the new dict"""

        # check if attrs is a list passed to our function
        if isinstance(attrs, list):
            # create an empty dictionary which will be returned
            attr_dict = {}
            # loop through attrs
            for atribs in attrs:
                # confirm self has attrs[atribs]
                if hasattr(self, atribs):
                    # getattr from self if it exists
                    attr_dict[atribs] = getattr(self, atribs)
            return attr_dict
        return self.__dict__

    def reload_from_json(self, json):
        """ reload_from will replace all attributes of the Student instance\
        example says "json" will always be a dictionary - with key and value,\
        so we can use json.items() to loop through the dict passed in, confrim\
        that that item[0] for items is present attr in Stuendt and\
        then set the attr to the key, value present for each item"""

        # loop through 'each' of json dicts .items()
        for each in json.items():
            # confirm 'each' key is attr of Student class
            if hasattr(self, each[0]):
                # set attributes of 'each' key and value to Student class
                setattr(self, each[0], each[1])
