#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for row in matrix:
        squared_row = []
        for element in row:
            if isintance(element, int):
                squared_row.append(element ** 2)
            else:
                squared_row.append(element)
        squared_matrix.append(squared_row)
    return squared_matrix
