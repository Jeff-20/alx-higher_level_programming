#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = [[1]] * len(matrix)
    i = 0
    for row in matrix:
        squared_matrix[i] = [x**2 for x in row]
        i += 1
    return (squared_matrix)
