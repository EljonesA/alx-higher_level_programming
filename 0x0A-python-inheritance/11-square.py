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
    def __init__(self, width, height):
        """
        Initializes a Rectangle object with the specified width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Computes area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a custom string representation of the rectangle.

        Returns:
        str: A string in the format '[Rectangle] <width>/<height>'.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    def __init__(self, size):
        """
        Initializes a Square object with the specified size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

        def __str__(self):
            """
            Returns a custom string representation of the square.

            Returns:
                str: A string in the format '[Rectangle] <size>/<size>'.
            """
            return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
