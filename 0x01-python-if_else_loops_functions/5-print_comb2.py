#!/usr/bin/python3
for i in range(100):
    if i == 99:
        print("{}\n".format(i))
        break;
    print("{}{},".format(0, i) if i < 10 else "{}, ".format(i), end="")
