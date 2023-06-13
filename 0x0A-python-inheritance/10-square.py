#!/usr/bin/python3

"""This module defines a class
    'Square' that inherits
     the class 'Rectangle'
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A class that inherits Rectangle, and
        with the attributes 'size' and 'area'
    """
    def __init__(self, size):
        super().__init__(size, size)
