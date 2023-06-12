#!/usr/bin/python3

"""This module defines a function that tells if
   an object is an instance of, or if the object
   is an instance of a class that inherited,
   a specified class
"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a a_class
       or a class that inherited a_class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
