#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    ''' A class define the Max_integer function '''

    def max_integer_test(self):
        ''' Test max_integer '''

        self.assertEqual(max_integer([10, 5, 3, 6, 9]), 10)
        self.assertEqual(max_integer([3, 5, 6, 9, 10]), 10)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1.2, 2.3, 5.6, 4.3]), 5.6)
        self.assertEqual(max_integer([ 2, 5, 3.1, 6.7]), 6.7)
        self.assertEqual(max_integer(['int', 'float', 'str']), 'str')

    def empty_list(self):
        ''' Test empty list '''

        _list = []
        self.assertIs(max_integer(_list), None)

if __name__ == '__main__':
    unittest.main()
