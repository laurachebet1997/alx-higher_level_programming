#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_square = []
    for x in matrix:
        new_square.append(list(map(lambda x: x**2, x)))
    return(new_square)
