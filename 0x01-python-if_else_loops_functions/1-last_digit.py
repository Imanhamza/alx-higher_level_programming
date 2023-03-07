#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_number = int(repr(number)[-1])

if number > 0:
    if l_number == 0:
        print(f"Last digit of {number} is 0 and is 0")
    elif l_number > 5:
        print(f"Last digit of {number} is {l_number} and is greater than 5")
    elif l_number < 6 and l_number != 0:
        print(f"Last digit of {number} is {l_number} and is less than 6 and not 0")
else:
    if l_number < 6 and l_number != 0:
        print(f"Last digit of {number} is {-l_number} and is less than 6 and not 0")

