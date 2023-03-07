#!/usr/bin/python3
def uppercase(str):
    for i in str:
        a = ord(i)
        if a >= 97 and a < 123:
            c = chr(a - 32)
            print("{}".format(c), end="")
    print("")
