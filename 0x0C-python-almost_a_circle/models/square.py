#!/usr/bin/python3
''' A class Square that inherits from Rectangle '''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' A class deals with a square '''

    def __init__(self, size, x=0, y=0, id=None):
        ''' A function to initate a suare '''

        super().__init__(size, size, x, y, id)

    # size setting

    @property
    def size(self):
        ''' A function to return the self value '''

        return self.width

    @size.setter
    def size(self, value):
        ''' setting the value of size '''

        self.width = value
        self.height = value

    # update __str__

    def __str__(self):
        ''' Update the str method with specific phrase '''

        i = self.id
        s = self.size
        _x = self.x
        _y = self.y
        return (f"[Square] ({i}) {_x}/{_y} - {s}")

    # assign attributes

    def update(self, *args, **kwargs):
        ''' Update attributes '''

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

    # Create a dictionary

    def to_dictionary(self):
        ''' A dictionary representation of a Square '''

        _dict = {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
        return _dict
