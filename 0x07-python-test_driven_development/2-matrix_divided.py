#!/usr/bin/python3
def matrix_divided(matrix, div):
    ''' A unction that divides all elements of a matrix. '''

    if div == 0:
        raise ZeroDivisionError('division by zero')
    elif type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')

    new_matrix =[]
    for i in matrix:
        if (len(i) != len(matrix[0])):
            raise TypeError('Each row of the matrix must have the same size')

        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        new_matrix = [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
    return new_matrix
