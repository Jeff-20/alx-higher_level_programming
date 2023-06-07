#!/usr/bin/python3


def add_integer(a, b=98):

    try:
        return int(a) + int(b)

    except:

        if type(a) is not int and float:
            raise TypeError("a must be an integer")

        elif type(b) is not int and float:
           raise TypeError("b must be an integer")
