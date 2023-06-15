#!/usr/bin/python3

"""This module defines function 'class_to_json'
    that returns dictionary description with simple
    data structure for JSON serialization of an object
"""


def class_to_json(obj):
    """Returns dictionary description of obj"""
    return obj.__dict__
