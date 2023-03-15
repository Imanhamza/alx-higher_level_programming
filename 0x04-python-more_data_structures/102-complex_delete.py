#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary and (value in a_dictionary.values()):
        for i in list(a_dictionary.keys()):
            if a_dictionary[i] == value:
                a_dictionary.pop(i)
    return a_dictionary
