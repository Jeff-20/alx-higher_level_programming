#!/usr/bin/python3

"""Defines class 'Base'
"""


import json


class Base:
    """Base class with the attributes __nb_objects and id
    """

    __nb_objects = 0

    def __init__(self, id=None):

        self.id = id

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of
            'list_dictionaries'
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return json.dumps(list_dictionaries)
