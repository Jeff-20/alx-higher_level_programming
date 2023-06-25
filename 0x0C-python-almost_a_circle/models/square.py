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

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Assigns attributes"""
        try:
            if args:
                self.id = args[0]
                self.size = args[1]
                self.__x = args[2]
                self.__y = args[3]
        except IndexError:
            pass
        finally:
            if kwargs.get('id'):
                self.id = kwargs['id']
            if kwargs.get('size'):
                self.size = kwargs['size']
            if kwargs.get('x'):
                self.__x = kwargs['x']
            if kwargs.get('y'):
                self.__y = kwargs['y']

    def to_dictionary(self):
        """returns the dictionary representaion of class 'Square'
        """
        obj = {'id': self.id, 'size': self.size, 'x': self.__x, 'y': self.__y}
        return obj
