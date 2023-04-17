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

        return (f"[Square] ({self.id}) {self.size}/{self.size} - {self.size}")
