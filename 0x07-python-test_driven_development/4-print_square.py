#!/usr/bin/python3

"""This module defines a 'print_square' function
    that prints a square with the # character
"""


def print_square(size):
    """Prints a square with # character"""

    if type(size) != int:
        raise TypeError("size must be an integer")

    elif size < 0:
        raise ValueError("size must be >= 0")

    elif type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):

        print("#"*size, end="")
        print()
