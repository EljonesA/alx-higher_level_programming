#!/usr/bin/python3
""" test module for Base class """

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test class for the Base class

    Methods:
        test_instance_with_id
        test_instance_without_id
        test_from_json_string
    """

    def test_instance_with_id(self):
        """ test method incase id provided """

        base = Base(10)
        self.assertEqual(base.id, 10)

    def test_instance_without_id(self):
        """ test method incase id not provided """

        base1 = Base()
        base2 = Base()

        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_from_json_string(self):
        """ test method for converting JSON representation """

        json_string = ('[{"id": 1, "width": 10, "height": 7}, '
                       '{"id": 2, "width": 5, "height": 5}]')
        result = Base.from_json_string(json_string)
        self.assertIsInstance(result, list)  # ensure result is a list

        # ensure that the list contains dictionaries
        for item in result:
            self.assertIsInstance(item, dict)

        # check content of the dictionaries
        self.assertEqual(result[0], {"id": 1, "width": 10, "height": 7})
        self.assertEqual(result[1], {"id": 2, "width": 5, "height": 5})
