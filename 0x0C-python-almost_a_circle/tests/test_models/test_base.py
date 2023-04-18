#!/usr/bin/python3
''' unittest for base.py '''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    ''' test for class Base '''

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)
    def remain_t(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

        with self.assertRaises(TypeError):
            Base(1, 2)

        self.assertEqual("hello", Base("hello").id)
        self.assertEqual(5.5, Base(5.5).id)
        self.assertEqual(complex(5), Base(complex(5)).id)
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)
        self.assertEqual(True, Base(True).id)
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)
        self.assertEqual((1, 2), Base((1, 2)).id)
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)
        self.assertEqual(range(5), Base(range(5)).id)
        self.assertEqual(b'Python', Base(b'Python').id)
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)
        self.assertEqual(float('inf'), Base(float('inf')).id)
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_from_json_string(self):
        ''' Test class for to_json_string function '''

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        with self.subTest():
            r1 = Rectangle(10, 7, 2, 8, 1)
            r1_dict = r1.to_dictionary()
            json_dict = Base.to_json_string([r1_dict])
            self.assertEqual(r1_dict, {
                'x': 2, 'width': 10,
                'id': 1, 'height': 7, 'y': 8})
            self.assertIs(type(r1_dict), dict)

        with self.assertRaises(TypeError):
            Base.to_json_string()

        with self.assertRaises(TypeError):
             Base.to_json_string([], 1)
