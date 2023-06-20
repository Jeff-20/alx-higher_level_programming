#!/usr/bin/python3

"""Defines class 'Base'
"""


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
