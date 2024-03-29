#!/usr/bin/python3

"""Defines a class 'Rectangle' that
    inherits class 'Base'
"""


from models.base import Base


class Rectangle(Base):

    """Inherits class 'Base' and has the attributes
        width, height, x, and y
    """

    def __init__(self, width, height, x=0, y=0, id=None):

        if type(width) != int:
            raise TypeError("width must be an integer")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if type(x) != int:
            raise TypeError("x must be an integer")
        if type(y) != int:
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute below"""

        try:
            if args is not None:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
        except IndexError:
            pass
        finally:
            if kwargs.get('id'):
                self.id = kwargs['id']
            if kwargs.get('width'):
                self.__width = kwargs['width']
            if kwargs.get('height'):
                self.__height = kwargs['height']
            if kwargs.get('x'):
                self.__x = kwargs['x']
            if kwargs.get('y'):
                self.__y = kwargs['y']

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Returns area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with
           the # character
        """
        for i in range(self.__y):
            print("")

        for i in range(self.__height):
            for i in range(self.__x):
                print(" ", end="")
            for i in range(self.__width):
                print("#", end="")
            print("")

    def to_dictionary(self):
        """returns dictionary representation of class 'Rectangle'
        """
        obj = {'width': self.__width, 'height': self.__height, 'x': self.__x,
               'y': self.__y, 'id': self.id}
        return obj

    def __str__(self):
        """Overridden str"""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} -\
 {self.__width}/{self.__height}")
