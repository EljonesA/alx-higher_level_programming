#!/usr/bin/python3
"""Unittests for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertIsNone(max_integer([])) # check if list is empty
        #self.assertEqual(max_integer([5]), 5) # 1 int
        self.assertEqual(max_integer([1, 3, 7, 2, 9]), 9) # +ves only
        self.assertEqual(max_integer([-1, -3, -7, -2, -9]), 9) # -ves only
        self.assertEqual(max_integer([1, 3, -7, 2, -9]), 3) # +ves & -ves
        self.assertEqual(max_integer([1.5, 2.7, 3.9]), 3.9) # float numbers
        self.assertEqual(max_integer([1.5, 2.7, 3]), 3) # ints & float
