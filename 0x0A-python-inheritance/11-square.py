#!/usr/bin/python3

"""This module defines a class
   'Square' that inherits
   the class 'Rectangle'
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits class 'Rectangle'"""

    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
