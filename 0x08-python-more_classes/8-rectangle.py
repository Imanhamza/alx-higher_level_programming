#!/usr/bin/python3
'''
A class Rectangle that defines a rectangle by: (based on 7-rectangle.py)
'''


class Rectangle:
    ''' Class to compute rectangle equations '''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        ''' initiation of a calss has args
        width (int): Private instance attribute
        height (int): Private instance attribute
        number_of_instances (int): Public instance attribute
        '''

        Rectangle.number_of_instances += 1
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
        # type(self).number_of_instances += 1

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

        # type(self).number_of_instances += 1
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

    # str to print #

    def __str__(self):
        '''
        print the # as the rectangle
        '''

        _print = ''
        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                _print += str(self.print_symbol)

            if i != self.__height - 1:
                _print += '\n'
        return _print

    # repr() to return a string representation of the rectangle

    def __repr__(self):
        '''
        return a string representation of the rectangle
        to be able to recreate a new instance
        '''

        return ("Rectangle({}, {})".format(self.__width, self.__height))

    # Deleting message

    def __del__(self):
        '''
        A goodbye message to Rectangle
        '''

        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    # find the biggest one

    def bigger_or_equal(rect_1, rect_2):
        '''
        A function to find the rectangle with the biggest area
        '''

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
