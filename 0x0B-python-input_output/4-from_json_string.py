#!/usr/bin/python3
''' A module returns an object returns an object '''
import json


def from_json_string(my_str):
    ''' A function to returns an object a JSON representation '''

    return json.loads(my_str)
