#!/usr/bin/python3
def add_integer(a, b=98):
    ''' A function to add two integers '''
    if (type(a) is not int) and (type(a) is not float):
        raise TypeError("a must be an integer")
    elif type(b) is not int and (type(b) is not float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
