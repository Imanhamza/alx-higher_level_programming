#!/usr/bin/python3
''' A module appends a string to a file a retuen len '''


def append_write(filename="", text=""):
    ''' A function to append a string and return the length '''

    with open(filename, 'a', encoding="utf-8") as _file:
        data = _file.write(text)
        return data
