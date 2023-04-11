#!/usr/bin/python3
'''
A module class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' A class to compute a Rectangle '''

    def __init__(self, width, height):
        ''' initiation of Rectangle class '''

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
