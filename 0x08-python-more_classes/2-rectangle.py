#!/usr/bin/python3
"""A functional implementation of an empty class"""


class Rectangle:
    """
    class implementation of the rectangle

    Attributes:
        __width (int): width of the rectangle
        __height (int): height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle instance.

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Getter method for the width attribute

        Returns:
            int: width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Seter method for the width attribute

        Args:
            value (int): new width value

        Raises:
            TypeError: width must be an integer
            ValueError: width must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute

        Returns:
            int: height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Args:
            value: new height value

        Raises:
            TypeError: height must be an integer
            ValueError: height must be > 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Computes area of the rectangle

        Returns:
            int: area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Computes perimeter of the rectangle

        Returns:
            int: perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
