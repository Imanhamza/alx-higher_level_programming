#!/usr/bin/python3
'''
A class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
(task based on 8-rectangle.py)
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

    def area(self):
        ''' A function computes the area '''
        return self.__width * self.__height

    def __str__(self):
        ''' A function to print out the lenght of rectangle '''
        return ('[Rectangle] {}/{}'.format(self.__width, self.__height))
