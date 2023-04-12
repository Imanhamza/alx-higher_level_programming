#!/usr/bin/python3
''' A module to read UTF8 and print it out '''


def read_file(filename=""):
    ''' A function to read a file and print int put '''

    with open(filename, encoding="utf-8") as _file:
        data = _file.read()
    print(data)
