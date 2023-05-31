#!/usr/bin/python3

"""This module contains a Square class that defines
    a square
"""


class Square:
    """Defines a square with the attribute "size"
    """
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """This method returns the area of a square"""
        return (self.__size)**2

    @property
    def size(self):
        """Retrieves the value of "size" """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the value of "size" """
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        """Prints square with # character to the standard output"""
        for i in range(self.__size):
            print("#" * self.__size)
