#!/usr/bin/python3

"""This module defines a class
    'BaseGeometry'
"""


class BaseGeometry:
    """A class with the attributes area and integer_validator"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
