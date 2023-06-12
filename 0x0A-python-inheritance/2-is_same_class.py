#!/usr/bin/python3

"""This module defines a function that tells
    if an object is exactly an instance of a
    specified class
"""


def is_same_class(obj, a_class):
    """Returns True if obj is an instance of a_class, otherwise False"""
    if type(obj) == a_class:
        return True
    else:
        return False
