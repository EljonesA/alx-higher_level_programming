#!/usr/bin/python3
"""Empty class"""


class BaseGeometry:
    """ Class with area method """

    def area(self):
        """
        Raises an Exception with custom message

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")
