#!/usr/bin/python3

"""This module defines 'matrix_divided' function
    that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix"""
    new_mat = []
    new_list = []
    try:
        for list in matrix:
            for item in list:

                new_list.append(round((item / div), 2))
            new_mat.append(new_list)
            new_list = []
        return new_mat

    except Exception:
        if type(matrix) != int or type(matrix) != float:
            raise TypeError("matrix must be a matrix(list of lists)\
                            of integers/float")

        elif len(matrix[l]) != len(matrix[l + 1]):
            raise TypeError("Each row of the matrix must have the same size")

        elif type(div) != int or type(div) != float:
            raise TypeError("div must be a number")
        else:
            if div == 0:
                raise ZeroDivisionError("division by zero")
