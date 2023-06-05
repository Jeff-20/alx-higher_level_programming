#!/usr/bin/python3

"""This module defines a class 'Rectangle'
"""


class Rectangle:
    """A Rectangle class with the attributes 'width'
       and 'height'
    """
    def __init__(self, width=0, height=0):
        
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):

        self.__width = value

        if type(value) is not int:
            raise TypeError("with must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):

        self.__height = value

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
