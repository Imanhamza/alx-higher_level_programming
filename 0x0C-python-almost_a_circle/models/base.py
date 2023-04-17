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

        if list_objs is None:
            list_objs = []

        _dict = []
        for i in list_objs:
            _dict.append(i.to_dictionary())

        with open(file_name, 'w') as _file:
            _file.write(Base.to_json_string(_dict))

    # list of the JSON string

    @staticmethod
    def from_json_string(json_string):
        ''' From JSON to dictionary '''

        if json_string is None or json_string == '[]':
            return []

        return json.loads(json_string)

    # Return all instances

    @classmethod
    def create(cls, **dictionary):
        ''' A function eturns an instance with all attributes already set '''

        if cls.__name__ == 'Rectangle':
            R = cls(5, 5)
        else:
            R = cls(5)

        R.update(**dictionary)
        return R

    # List of all intances

    def load_from_file(cls):
        ''' A function returns a list of instances '''

        file_name = cls.__name__ + '.json'
        
        try:
            _file = open(filename, 'r')
        except FileNotFoundError:
            return []
        else:
            _dict = Base.from_json_string(_file.read())

            _list = []
            for i in _dict:
                _list.append(cls.create(**i))
            _file.close()
            return _list
