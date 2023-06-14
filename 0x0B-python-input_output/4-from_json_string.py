#!/usr/bin/python3

"""This module defines fucntion 'from_json_string'
    an object (Python data structure)
    represented by a JSON string
"""


import json


def from_json_string(my_str):
    """Returns an object represented by JSON string 'my_str'
    """
    return json.loads(my_str)
