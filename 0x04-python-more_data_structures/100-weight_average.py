#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        top = 0
        bottom = 0
        for i in my_list:
            mul = 1
            for j in range(len(i)):
                mul *= i[j]
                if j == 1:
                    bottom += i[j]
            top += mul
        return top / bottom
    return 0
