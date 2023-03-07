#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        c = chr(ord(str[i]) - 32)
        print("{}".format(c) if ord(str[i]) >= 97 and ord(str[i]) < 123
                else "{}".format(str[i]), end="")
    print("")
