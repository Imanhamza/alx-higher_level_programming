#!/usr/bin/python3
''' A module for escription with simple data structure '''


def class_to_json(obj):
    ''' A function returns a dictionary of decription '''

    return obj.__dict__
