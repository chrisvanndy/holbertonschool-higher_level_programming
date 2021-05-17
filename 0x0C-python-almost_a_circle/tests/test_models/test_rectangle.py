#!/usr/bin/python3
"""Test Module for base.rectangle()"""


import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """TestRectangle class, tests the Rectangle class""" 

    def test_rect_2(self):
        rect = Rectangle(2, 4)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 4)

    def test_rect_4(self):
        rect = Rectangle(2, 4, 2, 4)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 4)

    def test_rect_5(self):
        rect = Rectangle(2, 4, 6, 8 , 10)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.x, 6)
        self.assertEqual(rect.y, 8)
        self.assertEqual(rect.id, 10)

    def test_rect_update(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(9, 2, 4, 5, 6)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 6)
        self.assertEqual(rect.id, 9)

    def test_rect_to_dict(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        r_to_dict = rect.to_dictionary()
        self.assertEqual(
            r_to_dict, {'width': 1, 'height' : 2, 'x': 3, 'y': 4, 'id': 5})

    def test_area(self):
        rect = Rectangle(2,4)
        self.assertEqual(rect.area(), 8)

    def test_string(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(rect), "[Rectangle] (5) 3/4 - 1/2")

    def test_rect_raises_VE(self):
        with self.assertRaises(ValueError):
            rect0 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            rect1 = Rectangle(2, 0)
        with self.assertRaises(ValueError):
            rect2 = Rectangle(-2, 4)
        with self.assertRaises(ValueError):
            rect3 = Rectangle(2, -4)
        with self.assertRaises(ValueError):
            rect4 = Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            rect5 = Rectangle(4, 3, 2, -1)

    def test_rect_raises_TE(self):
        with self.assertRaises(TypeError):
            rect0 = Rectangle("2", 4)
        with self.assertRaises(TypeError):
            rect1 = Rectangle(2, "4")
        with self.assertRaises(TypeError):
            rect2 = Rectangle(3, 2, "1")
        with self.assertRaises(TypeError):
            rect3 = Rectangle(1, 2, 3, "4")


