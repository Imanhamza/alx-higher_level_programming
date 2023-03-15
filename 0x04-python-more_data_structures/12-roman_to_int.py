#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
    if roman_string:
        # get the length of the string
        len_s = len(roman_string)
        # get the last number value
        result = roman[roman_string[len_s - 1]]
        # loop over the string to find the previous numbers
        for i in range(len_s - 1, 0, -1):
            # set the values of the current and previous integer
            current = roman[roman_string[i]]
            prev = roman[roman_string[i - 1]]

            # check the relation between two values
            if current > prev:
                result -= prev
            else:
                result += prev
        return result
    return 0
