#!/usr/bin/python3

"""This module defines a function that returns a
   list of available attributes and methods of an
   object
"""


def lookup(obj):
    """Returns attributes and methods of obj"""
    return dir(obj)
