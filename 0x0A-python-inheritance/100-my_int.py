#!/usr/bin/python3

"""Defines class 'MyInt' that inherits int"""


class MyInt(int):
    """inherits int"""
    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return True
