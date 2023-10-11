#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    else:
        return [[element**2 for element in row] for row in matrix]
