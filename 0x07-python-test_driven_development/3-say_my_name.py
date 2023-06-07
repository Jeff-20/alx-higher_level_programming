#!/usr/bin/python3

"""This module defines 'say_my_name' function
    that prints My name is <first_name> <last_name>
"""


def say_my_name(first_name, last_name=""):
    """Prints 'My name is <first_name> <last_name>"""

    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    elif type(last_name) != str:
        raise TypeError("last_name must be a string")

    else:
        print(f"My name is {first_name} {last_name}")
