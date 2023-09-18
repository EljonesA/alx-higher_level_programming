#!/usr/bin/python3
""" module to test the square class and its methods"""

import unittest
from models.square import Square
from models.base import Base
# import os


class TestSquare(unittest.TestCase):
    """
    Class for our unittest methods

    Methods:
        test_create_square
        tests_invalid_size
        test_set_size
        test_set_invalid_size
        test_set_valid_size
        test_string_representation >> needs FIX
        test-to_dictionary
    """

    def test_create_square(self):
        """ create square test """

        s = Square(4)
        self.assertEqual(s.size, 4)

    def test_invalid_size(self):
        """ method for testing provided size of the square """

        with self.assertRaises(ValueError) as context:
            s = Square(-4)
        self.assertEqual(str(context.exception), "width must be > 0")

        with self.assertRaises(ValueError) as context:
            s = Square(0)
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_set_size(self):
        """ method for testing provided size of the square """

        s = Square(4)
        s.size = 6
        self.assertEqual(s.size, 6)
        self.assertEqual(s.width, 6)
        self.assertEqual(s.height, 6)

    def test_set_invalid_size(self):
        """ method for testing provided size of the square """

        s = Square(4)
        with self.assertRaises(ValueError) as context:
            s.size = -7
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_set_valid_size(self):
        """ method for testing provided size of the square """

        s = Square(4)
        s.size = 7
        self.assertEqual(s.size, 7)

    """
    def test_string_representation(self):
        """ """test method for __str__ """
    """    s = Square(5)
        self.assertEqual(str(s), "[Square] (7) 0/0 - 5")
    """

    def test_to_dictionary(self):
        """ test method for creating dict representation of our class """

        s = Square(5, 2, 3, 1)
        dictionary = s.to_dictionary()
        expected_outcome = {
                'id': 1,
                'x': 2,
                'size': 5,
                'y': 3
                }
        self.assertEqual(dictionary, expected_outcome)

    # test_load_from_file
    """@classmethod
    def setUpClass(cls):
        cls.test_filename = "test_filename.json"

    def tearDown(self):
        try:
            os.remove(self.test_filename)
        except FileNotFoundError:
            pass

    def test_load_from_file(self):
        with open(self.test_filename, "w") as file:
            file.write('[{"id": 1, "width": 10, "height": 7}, '
            '{"id": 2, "width": 5, "height": 5}]')

        instances = Base.load_from_file() # load instance from test JSON file
        self.assertIsInstance(instances, list)
        self.assertEqual(len(instances), 2) # check the number of instances

        # ensure list contains instances of Base or its subclasses
        for item in instances:
            self.assertIsInstance(item, Base)

        # check contents of the instances
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[0].width, 10)
        self.assertEqual(instances[0].height, 7)
        self.assertEqual(instances[1].id, 2)
        self.assertEqual(instances[1].width, 5)
        self.assertEqual(instances[1].height, 5)"""
