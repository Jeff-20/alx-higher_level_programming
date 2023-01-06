#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value != round(value):
            if value < 0:
                raise ValueError
                print('width must be >= 0')
            raise TypeError
            print('width must be an integer')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value != round(value):
            if value < 0:
                raise ValueError
                print('height must be >= 0')
            raise TypeError
            print('height must be an integer')
        self.__height = value
