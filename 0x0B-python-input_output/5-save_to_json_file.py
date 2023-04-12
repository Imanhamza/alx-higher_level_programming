#!/usr/bin/python3
''' A module writes an Object to a text file '''
import json


def save_to_json_file(my_obj, filename):
    '''
    A function writes an Object to a text file, using a JSON representation
    '''

    with open(filename, 'w', encoding = "utf-8")as _file:
        return json.dump(my_obj, _file)
