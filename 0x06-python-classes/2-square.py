#!/usr/bin/python3
""" Module with a square class """


class Square:
    """
    This class defines a square.

    Attributes:
       __size (int): The size of the square (private)

    Methods:
       __init__(self, size=0): Initializes a new Square instance.

    """

    def __init__(self, size=0):
        """
        Initializes a new square instance.

        Args:
            size (int, optional): The size of the square. Defaults set to 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
