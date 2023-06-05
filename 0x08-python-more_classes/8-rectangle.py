#!/usr/bin/python3

"""This module defines a class 'Rectangle'
"""


class Rectangle:
    """A Rectangle class with the attributes 'width'
       and 'height'
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (self.__width*2) + (self.__height*2)

        if width or height == 0:
            return 0

    def __str__(self):
        string = ""

        if self.__width == 0 or self.__height == 0:
            return string

        for i in range(self.__height):
            string += (str(self.print_symbol) * self.__width)
            if i < self.__height - 1:
                string += '\n'
        return string

    def __repr__(self):
        return "{self.__class__.__name__}({self.width}, {self.height})".\
                 format(self=self)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
