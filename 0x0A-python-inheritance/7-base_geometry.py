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

    def integer_validator(self, name, value):
        """
        Validates a value

        Args:
            name: a string
            value: int to validate

        Raises:
            TypeError: value must be an integer
            ValueError: Value must be >= 0
        """
        self.name = name
        self.value = value

        if not(isinstance(value, int)):
            raise TypeError(f"{self.name} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
