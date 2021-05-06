#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ This class will run unit  tests for the max_integher func """
    def test_end(self):
        """ Tests the max integer on the end of a list """
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_middle(self):
        """tests a max int somewhere in middle of list """
        self.assertEqual(max_integer([1, 2, 3, 2, 1]), 3)
        self.assertEqual(max_integer([4, 5, 6, 3, 2]), 6)

    def test_random(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([-5, -3, -2, 0, 10]), 10)
        self.assertRaises(TypeError, max_integer("string"))
        self.assertRaises(TypeError, max_integer((1, 2)))
        self.assertRaises(TypeError, max_integer([2.0, 1]))
