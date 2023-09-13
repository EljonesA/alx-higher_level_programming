#!/usr/bin/python3
""" Module with square class definition """


class Square:
    """
    This class defines a square.

    Attributes:
        __size (int): The size of the square (private)

    Methods:
        __init__(self, size): Initializes a new Square instance.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """

        self.__size = size
