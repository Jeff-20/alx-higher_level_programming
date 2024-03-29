#!/usr/bin/python3

"""This module defines function 'read_file'
    that reads a text file (UTF8) and prints
    it to the STDOUT
"""


def read_file(filename=""):
    """Reads 'filename' and prints its content to
        STDOUT
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
