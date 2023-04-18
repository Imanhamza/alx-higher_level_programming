#!/usr/bin/python3
''' unittest for Square.py '''
import unittest
from random import randrange
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    ''' test for Square Class '''

    def square_test(self):

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("int")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)

        self.assertIsInstance(Square(15), Base)
        self.assertIsInstance(Square(15), Square)

        self.assertEqual(5, Square(5, 2, 3, 9).size)
