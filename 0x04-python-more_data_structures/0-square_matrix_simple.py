#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    outer_array = []
    for i in matrix:
        inner_array = []
        for j in i:
            inner_array.append(j**2)
        outer_array.append(inner_array)
    return outer_array
