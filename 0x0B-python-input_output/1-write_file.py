#!/usr/bin/python3
''' A module to write to a file and return the len of the string '''


def write_file(filename="", text=""):
    ''' A function to add a string to a file with write and return len '''

    with open(filename, 'w', encoding="utf-8") as _file:
        data = _file.write(text)
        return len(text)
