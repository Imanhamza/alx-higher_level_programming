#!/usr/bin/python3
'''
A class Rectangle that defines a rectangle by: (based on 1-rectangle.py)
'''


class Rectangle:
    ''' Class to compute rectangle equations '''

    def __init__(self, width=0, height=0):
        '''
        initiation of a calss has args
        width (int): Private instance attribute
        height (int): Private instance attribute
        '''

        self.width = width
        self.height = height

    # Start setting width

    @property
    def width(self):
        ''' A function to retrive the width '''

        return self.__width

    @width.setter
    def width(self, value):
        ''' A function to set the value of the width '''

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    # Start setting height

    @property
    def height(self):
        ''' A function to retrive the height '''

        return self.__height

    @height.setter
    def height(self, value):
        ''' A function to set the height '''

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    # compute the area (width * height)

    def area(self):
        ''' A function to retrive the area '''

        return self.__width * self.__height

    # compute the perimeter (2(width + height))

    def perimeter(self):
        ''' A function to compute the premiter '''

        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width + self.__height) * 2
