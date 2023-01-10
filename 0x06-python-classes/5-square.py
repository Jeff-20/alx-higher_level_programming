#!/usr/bin/python3
"""
This is a class that defines a square
"""


class Square:
    """class Square with size attribute"""
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return (self.__size)**2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        res = ""
        if self.__size == 0:
            print(res)
        for i in range(self.__size):
            res += ('#' * self.__size)
            if i != (self.__size - 1):
                res += "\n"
        print(res)
