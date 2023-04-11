#!/usr/bin/python3
''' A module for inherting a list '''


class MyList(list):
    ''' A class defines a funtion to inhert the list '''

    def print_sorted(self):
        ''' A function to print the list '''

        _sorted = sorted(self)
        print(_sorted)
