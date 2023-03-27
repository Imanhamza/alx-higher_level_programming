#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    list_len = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (IndexError, TypeError):
            pass
        else:
            list_len += 1
    print()
    return list_len
