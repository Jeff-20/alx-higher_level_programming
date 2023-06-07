#!/usr/bin/python3

"""This module defines 'add_integer' function
    that adds two integers
"""


def add_integer(a, b=98):
    """Adds two integers"""
    try:
        return int(a) + int(b)

    except Exception:

        if type(a) is not int and float:
            raise TypeError("a must be an integer")

        elif type(b) is not int and float:
            raise TypeError("b must be an integer")
