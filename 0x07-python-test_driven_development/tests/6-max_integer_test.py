#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    ''' A class define the Max_integer function '''

    def unorder_list(self):
        ''' Test unordered list '''

        _list = [5, 3, 6, 10, 9]
        self.assertEqual(max_integer(_list), 10)

    def ordered_list(self):
        ''' Test ordered list '''

        _list = [3, 5, 6, 9, 10]
        self.assertEqual(max_integer(_list), 10)

    def empty_list(self):
        ''' Test empty list '''

        _list = []
        self.assertIs(max_integer(_list), None)

    def one_element(self):
        ''' Test list with one element '''

        _list = [1]
        self.assertEqual(max_integer(_list), 1)

    def floats_list(self):
        ''' Test list with floats '''

        _list = [1.2, 2.3, 5.6, 4.3]
        self.assertEqual(max_integer(_list), 5.6)

    def floats_int(self):
        ''' Test list with integers and floats '''

        _list = [ 2, 5, 3.1, 6.7]
        self.assertEqual(max_integer(_list), 6.7)

    def string_list(self):
        ''' Test list with strings '''

        _list = ['int', 'float', 'str']
        self.assertEqual(max_integer(_list), 'str')
if __name__ == '__main__':
    unittest.main()
