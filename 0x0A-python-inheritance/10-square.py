#!/usr/bin/python3
'''
A class Square that inherits from Rectangle (9-rectangle.py).
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    ''' A class deals with a square '''

    def __init__(self, size):
        ''' A function to initate a suare '''

        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        ''' A function computes the area of a square '''
        return self.__size**2

    def __str__(self):
        ''' Print out the details '''
        return ('[Rectangle] {}/{}'.format(self.__size, self.__size))
