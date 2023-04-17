#!/usr/bin/python3
''' A class Rectangle that inherits from Base '''
from models.base import Base


class Rectangle(Base):
    ''' class Rectangle that inherits from Base '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' initiation of the class attributes '''

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        ''' A function to retrive the width '''

        return self.__width

    @width.setter
    def width(self, value):
        ''' A function to set the value of the width '''

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

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
        elif value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    # Start setting x

    @property
    def x(self):
        ''' A function to retrive x '''

        return self.__x

    @x.setter
    def x(self, value):
        ''' A function to set x '''

        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    # Start setting y

    @property
    def y(self):
        ''' A function to retrive y'''

        return self.__y

    @y.setter
    def y(self, value):
        ''' A function to set y '''

        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value
