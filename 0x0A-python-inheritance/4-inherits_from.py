#!/usr/bin/python3

"""This module defines a function that tells
    if an object is an instance of a class that
    that inherited (directly or indirectly) a
    specified class
"""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a class
        that inherited a_class
    """
    if (type(obj) != a_class) and issubclass(type(obj), a_class):
        return True
    else:
        return False
