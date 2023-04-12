#!/usr/bin/python3
''' A function def pascal_triangle(n) '''


def pascal_triangle(n):
    ''' A function returns a list of lists of integers
    representing the Pascal’s triangle
    '''

    _list = []

    for i in range(n):
        row = [1]

        if i > 0:
            prev_row = _list[i - 1]
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j + 1])
            row.append(1)
        _list.append(row)
    return _list
