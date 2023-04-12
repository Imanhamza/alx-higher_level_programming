#!/usr/bin/python3
''' A class Student that defines a student by: (based on 9-student.py) '''


class Student:
    ''' A class Student with args:
    first_name(str): Public instance attribute
    last_name(str): Public instance attribute
    age(int): Public instance attribute
    '''

    def __init__(self, first_name, last_name, age):
        ''' initiation of the class '''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        ''' A function returns a dictionary of decription '''

        if type(attr) == list:
            dic = {i: self.__dict__[i] for i in self.__dict__.keys() & attr}
            return dic
        return self.__dict__
