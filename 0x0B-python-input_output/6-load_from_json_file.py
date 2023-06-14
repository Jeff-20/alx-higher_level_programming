#!/usr/bin/python3

"""This module defines function 'load_from_json_file'
    that creates an object from a JSON file
"""


import json


def load_from_json_file(filename):
    """Creates an object from JSON file 'filename'
    """
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
