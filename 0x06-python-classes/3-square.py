#!/usr/bin/python3

"""This module contains a Square class that defines
    a square
"""


class Square:
    """Defines a square with the attribute "size"
    """
    def __init__(self, size=0):
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """This method returns the area of a square"""
        return (self.__size)**2
