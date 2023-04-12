#!/usr/bin/python3
'''
A class Square that inherits from Rectangle (9-rectangle.py)
(task based on 10-square.py).
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' A class deals with a square '''

    def __init__(self, size):
        ''' A function to initate a suare '''

        super().integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        ''' A function computes the area os a square '''
        return self.__size**2

    def __str__(self):
        ''' print '''
        return ('[Square] {}/{}'.format(self.__size, self.__size))
