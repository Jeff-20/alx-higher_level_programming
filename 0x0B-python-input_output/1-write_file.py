#!/usr/bin/python3

"""This module defines function 'write_file'
    that writes a string to a text file (UTF8)
    and returns the number of characters written
"""


def write_file(filename="", text=""):
    """Writes a string 'text' to a text file 'filename'
        and returns the number of characters written
    """
    with open(filename, 'w', encoding='utf8') as f:
        return (f.write(text))
