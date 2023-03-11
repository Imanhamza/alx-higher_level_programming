#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < len(my_list) and idx >= 0:
        for i in my_list:
            if i == my_list[idx]:
                my_list.remove(i)
        return my_list
    else:
        return my_list
