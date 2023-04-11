#!/usr/bin/python3
''' A module to check if their is a direct inheritance '''


def inherits_from(obj, a_class):
    ''' A function to return True or False on direct inhritance '''

    return isinstance(obj, a_class) and type(obj) != a_class
