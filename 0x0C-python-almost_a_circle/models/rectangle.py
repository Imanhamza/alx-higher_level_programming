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

    # compute the area (width * height)

    def area(self):
        ''' A function to retrive the area '''

        return self.__width * self.__height

    # display the shape of rectangle with #

    def display(self):
        ''' Display the shape of the rectangle '''

        # _print = []
        if self.__width == 0 or self.__height == 0:
            print("")

        for h in range(self.y):
            print()

        for i in range(self.height):
            for k in range(self.x):
                print(' ', end='')
            for j in range(self.width):
                print("#", end='')
            print()

    # update __str__

    def __str__(self):
        ''' A function returns a static phrase '''
        i = self.id
        w = self.__width
        h = self.__height
        _x = self.__x
        _y = self.__y
        return (f"[Rectangle] ({i}) {_x}/{_y} - {w}/{h}")

    # Assign the arguments

    def update(self, *args, **kwargs):
        ''' A function assigns an argument to each attribute '''

        if args and len(args) != 0:
            for i in range(len(args)):
                try:
                    self.id = args[0]
                    self.width = args[1]
                    self.height = args[2]
                    self.x = args[3]
                    self.y = args[4]
                except IndexError:
                    pass
        for key, value in kwargs.items():
            self.__setattr__(key, value)
        return

    # update rectangle with a dictionary

    def to_dictionary(self):
        ''' A dictionary representation of a Rectangle '''

        _dict = {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
        return _dict
