#!/usr/bin/python3

"""This module defines a class MyList that inherits
    from 'list'
"""


class MyList(list):
    """MyList inherits from list"""
    def print_sorted(self):
        print(sorted(self))
