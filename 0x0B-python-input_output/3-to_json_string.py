#!/usr/bin/python3
''' A module returns the JSON representation of an object (string) '''
import json


def to_json_string(my_obj):
    ''' A function to return the JSON of an object '''

    return json.dumps(my_obj)
