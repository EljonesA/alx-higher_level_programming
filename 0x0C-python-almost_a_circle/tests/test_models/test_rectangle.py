#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Class for the rectangle test methods

    Methods:
        test_create_rectangle
        tests_invalid_width
        test_set_invalid_width
        test_set_valid_width
        tests_invalid_height
        test_set_invalid_height
        test_set_valid_height
        tests_invalid_x
        test_set_invalid_x
        test_set_valid_x
        tests_invalid_y
        test_set_invalid_y
        test_set_valid_y
        test_area_method
        test_to_dictionary
        test_to_json_string
        test_string_representation >> needs FIX
    """
    def test_create_rectangle(self):
        """ test method fro creating a rectangle instance """

        # test values
        r = Rectangle(2, 3)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)

    def test_invalid_width(self):
        """ test method for setting width """

        with self.assertRaises(ValueError) as context:
            r = Rectangle(-2, 3)
        self.assertEqual(str(context.exception), "width must be > 0")

        with self.assertRaises(ValueError) as context:
            r = Rectangle(0, 3)
        self.assertEqual(str(context.exception), "width must be > 0")

        with self.assertRaises(TypeError) as context:
            r = Rectangle("2", 3)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_set_invalid_width(self):
        """ test method for setting width """

        r = Rectangle(2, 3)
        with self.assertRaises(ValueError) as context:
            r.width = -2
        self.assertEqual(str(context.exception), "width must be > 0")

        with self.assertRaises(ValueError) as context:
            r.width = 0
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_set_valid_width(self):
        """ test method for setting width """

        r = Rectangle(2, 3)
        r.width = 5
        self.assertEqual(r.width, 5)

    def test_invalid_height(self):
        """ test method for setting height """

        with self.assertRaises(ValueError) as context:
            r = Rectangle(2, -3)
        self.assertEqual(str(context.exception), "height must be > 0")

        with self.assertRaises(ValueError) as context:
            r = Rectangle(2, 0)
        self.assertEqual(str(context.exception), "height must be > 0")

        with self.assertRaises(TypeError) as context:
            r = Rectangle(2, "3")
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_set_invalid_height(self):
        """ test method for setting height """

        r = Rectangle(2, 3)
        with self.assertRaises(ValueError) as context:
            r.height = -3
        self.assertEqual(str(context.exception), "height must be > 0")

        with self.assertRaises(ValueError) as context:
            r.height = 0
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_set_valid_height(self):
        """ test method for setting height """

        r = Rectangle(2, 3)
        r.height = 5
        self.assertEqual(r.height, 5)

    def test_invalid_x(self):
        """ test method for setting x """

        with self.assertRaises(ValueError) as context:
            r = Rectangle(2, 3, -1, 4)
        self.assertEqual(str(context.exception), "x must be >= 0")

        with self.assertRaises(TypeError) as context:
            r = Rectangle(2, 3, "1", 4)
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_set_invalid_x(self):
        """ test method for setting x """

        r = Rectangle(2, 3)
        with self.assertRaises(ValueError) as context:
            r.x = -1
        self.assertEqual(str(context.exception), "x must be >= 0")

    def test_set_valid_x(self):
        """ test method for setting x """

        r = Rectangle(2, 3)
        r.x = 4
        self.assertEqual(r.x, 4)

    def test_invalid_y(self):
        """ test method for setting y """

        with self.assertRaises(ValueError) as context:
            r = Rectangle(2, 3, 1, -4)
        self.assertEqual(str(context.exception), "y must be >= 0")

        with self.assertRaises(TypeError) as context:
            r = Rectangle(2, 3, 1, "4")
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_set_invalid_y(self):
        """ test method for setting y """

        r = Rectangle(2, 3)
        with self.assertRaises(ValueError) as context:
            r.y = -1
        self.assertEqual(str(context.exception), "y must be >= 0")

    def test_set_valid_y(self):
        """ test method for setting y """

        r = Rectangle(2, 3)
        r.y = 7
        self.assertEqual(r.y, 7)

    def test_area_method(self):
        """ test method for calculating area of the rectangle """

        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

    # >>> Rewrite this test method. It prints to stdout instead of testing <<<
    """def test_display_method(self):
        r1 = Rectangle(2, 2)
        expected_output = "##\n##\n"
        self.assertEqual(r1.display(), expected_output)"""

    def test_to_dictionary(self):
        """ test method for creating dict representation of the rectangle """

        r = Rectangle(10, 7, 2, 8, 1)
        dictionary = r.to_dictionary()
        expected_output = {
                'x': 2,
                'y': 8,
                'id': 1,
                'height': 7,
                'width': 10
                }
        self.assertEqual(dictionary, expected_output)

    def test_to_json_string(self):
        """ test method for creating JSON representation of data """

        rectangles = [
                {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8},
                {'id': 2, 'width': 5, 'height': 5, 'x': 0, 'y': 0}
                ]
        json_string = Rectangle.to_json_string(rectangles)
        expected = ('[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, '
                    '{"id": 2, "width": 5, "height": 5, "x": 0, "y": 0}]')
        self.assertEqual(json_string, expected)

    """
    def test_string_representation(self):
        r = Rectangle(2, 3)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 2/3")
    """
