#!/usr/bin/python3
''' A class Rectangle that inherits from Base '''
from models.base import Base


class Rectangle(Base):
    ''' class Rectangle that inherits from Base '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' initiation of the class attributes '''

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
