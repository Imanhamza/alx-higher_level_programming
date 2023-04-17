#!/usr/bin/python3
''' A class Base '''


class Base:
    ''' A class Base with args:
    __nb_objects(int): private class attribute
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        ''' initiation of the class '''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
