#!/usr/bin/python3
'''
Definition of a class Square that
defines a square by: (based on 3-square.py)
'''


class Square:
    ''' A class dealing with a Square '''

    def __init__(self, size):
        ''' initiation of a calss has args
        size (int): Private instance attribute
        '''

        # check if the size int or not
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        # set the attribute
        self.__size = size

    @property
    def size(self):
        '''
        retrive the size
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        set the value of the property
        '''
        self.__size = value

    def area(self):
        '''
        returns the area of the Square
        '''
        return self.__size**2
