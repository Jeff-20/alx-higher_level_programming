#!/usr/bin/python3

"""This module defines function 'to_json_string'
    that returns the JSON representation of an
    object(string)
"""


import json


def to_json_string(my_obj):
    """Returns JSON representation of object 'my_obj'(string)
    """
    return json.dumps(my_obj)
