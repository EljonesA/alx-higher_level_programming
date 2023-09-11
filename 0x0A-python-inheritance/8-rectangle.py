#!/usr/bin/python3
"""Empty class"""


class BaseGeometry:
    """
    Base class for geometry operations

    Public methods:
    - area(): raises an exception
    - integer_validator(name, value): validates an int
    """

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

        args:
            name (str): a string
            value (int): int to validate

        Raises:
            TypeError: value must be an integer
            ValueError: Value must be >= 0
        """
        if not(isinstance(value, int)):
            raise TypeError(f"{self.name} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A subclass that inherits from BaseGeometry

    Args:
        width (int): of the rectangle
        height (int): of the rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
