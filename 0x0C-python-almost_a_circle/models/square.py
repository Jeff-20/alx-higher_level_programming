#!/usr/bin/python3

"""This module provides class 'Square' that
   inherits class 'Rectangle'
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits class 'Rectangle'
    """
    def __init__(self, size, x=0, y=0, id=None):
        self.__width = size
        self.__height = size
        self.__x = x
        self.__y = y

        super().__init__(self.__width, self.__height, self.__x, self.__y, id)

    def __str__(self):
        """returns human-readable object"""
        return f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.__width}"
