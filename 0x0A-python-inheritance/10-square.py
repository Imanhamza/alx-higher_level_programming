#!/usr/bin/python3
'''
A class Square that inherits from Rectangle (9-rectangle.py).
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(.Rectangle):
    ''' A class deals with a square '''

    def __init__(self, size):
        ''' A function to initate a suare '''

        self.__size = size
        super().__init__(self.__size, self.__size)

