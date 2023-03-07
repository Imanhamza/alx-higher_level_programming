#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 100):
        if i % 3 == 0 and i % 5 != 0:
            if i == 99:
                print("Fizz")
                break
            print("Fizz ", end="")
        elif i % 5 == 0 and i % 3 != 0:
            print("Buzz ", end="")
        elif i % 15 == 0:
            print("FizzBuzz ", end="")
        else:
            print("{} ".format(i), end="")
