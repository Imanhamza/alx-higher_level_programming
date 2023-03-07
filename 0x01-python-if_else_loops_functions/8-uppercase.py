#!/usr/bin/python3
def uppercase(str):
    for i in str:
        a = ord(i)
        if a >= 97 and a <= 123:
            i = chr(a - 32)
        print("{}".format(i), end="")
    print("")
