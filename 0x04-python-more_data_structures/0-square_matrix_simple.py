#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    for i in matrix:
        for l in matrix[i]:
            new_mat = [l**2 for l in matrix]
        return new_mat
    
