#!/usr/bin/python3
''' A module to print a square '''


def print_square(size):
    '''
    A function to print out a '#' square
    args:
    size (int): the length of the faces
    '''

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    if size == 0:
        return
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
