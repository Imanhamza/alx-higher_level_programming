#!/usr/bin/python3
''' A class Base '''
import json


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

    # JSON string representation

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' A representation of string '''

        if list_dictionaries is None or list_dictionaries == []:
            return '[]'

        return json.dumps(list_dictionaries)

    # list_dictionaries

    @classmethod
    def save_to_file(cls, list_objs):
        ''' writes the JSON string representation of list_objs to a file '''

        file_name = cls.__name__ + '.json'

        _dict = []
        for i in list_objs:
            i = i.to_dictionary()
            _dict_json = json.loads(Base.to_json_string(i))
            _dict.append(_dict_json)

        with open(file_name, 'w')as _file:
            json.dump(_dict, _file)
