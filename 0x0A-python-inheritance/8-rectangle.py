#!/usr/bin/python3

"""This module defines a class
    'Rectangle' that inherits
     the class 'BaseGeometry'
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A class that inherits BaseGeometry, and
        with the attributes 'width' and 'height'
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
