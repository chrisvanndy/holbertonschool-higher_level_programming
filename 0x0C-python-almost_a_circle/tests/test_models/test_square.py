#!/usr/bin/python3
"""TestSquare module tests the class Square"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """TestSquare unit tests for class Square"""

    def test_square_1(self):
        sqr = Square(1)
        self.assertEqual(sqr.size, 1)

    def test_square_xy(self):
        sqr = Square(1, 2, 3)
        self.assertEqual(sqr.size, 1)
        self.assertEqual(sqr.x, 2)
        self.assertEqual(sqr.y, 3)

    def test_square_xy_id(self):
        sqr = Square(4, 1, 2, 5)
        self.assertEqual(sqr.size, 4)
        self.assertEqual(sqr.x, 1)
        self.assertEqual(sqr.y, 2)
        self.assertEqual(sqr.id, 5)

    def test_square_update(self):
        sqr = Square(1, 1, 1, 1)
        sqr.update(10, 5, 2, 2)
        self.assertEqual(sqr.id, 10)
        self.assertEqual(sqr.size, 5)
        self.assertEqual(sqr.x, 2)
        self.assertEqual(sqr.y, 2)

    def test_square_to_dict(self):
        sqr = Square(1, 2, 3, 4)
        s_to_dict = sqr.to_dictionary()
        self.assertEqual(
            s_to_dict, {'size': 1, 'x': 2, 'y': 3, 'id': 4})

    def test_area(self):
        sqr = Square(5)
        self.assertEqual(sqr.area(), 25)

    def test_sqr_raises_VE(self):
        with self.assertRaises(ValueError):
            sqr0 = Square(0)
        with self.assertRaises(ValueError):
            sqr1 = Square(-1)
        with self.assertRaises(ValueError):
            sqr2 = Square(2, -1, 1)
        with self.assertRaises(ValueError):
            sqr3 = Square(2, 1, -1)

    def test_sqr_raises_TE(self):
        with self.assertRaises(TypeError):
            sqr0 = Square("S")
        with self.assertRaises(TypeError):
            sqr1 = Square(5, "x", 1)
        with self.assertRaises(TypeError):
            sqr2 = Square(4, 1, "y")
        
