#!/usr/bin/python3
''' vi class BaseGeometry (based on 6-base_geometry.py). '''


class BaseGeometry:
    ''' A class computes BaseGeometry '''

    def area(self):
        ''' A function raises an Execption '''

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' A function to validate an integer '''

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
