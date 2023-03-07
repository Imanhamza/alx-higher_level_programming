#!/usr/bin/python3
def uppercase(str):
    for i in str:
        a = ord(i)
        c = chr(a - 32)
        print("{}".format(c) if a >= 97 and a < 123 else "{}".format(i),
                end="")
    print("")
