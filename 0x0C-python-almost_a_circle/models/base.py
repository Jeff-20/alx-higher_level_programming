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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of
            'list_dictionaries'
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON representation of list_objs to a file
        """
        json_string = Base.to_json_string(list_objs)
        with open("Rectangle.json", "w", encoding=utf-8) as f:
           write(json.load(json_string))
