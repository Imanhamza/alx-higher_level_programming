#!/usr/bin/python3
''' A class MyInt that inherits from int '''


class MyInt(int):
    ''' A class deals with int '''

    def __eq__(self, second):
        ''' rewitrs the equalizer thing '''

        return int(self) != int(second)

    def __ne__(self, second):
        ''' rewrotes the Non-equal function '''

        return int(self) == int(second)
