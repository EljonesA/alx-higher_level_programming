#!/usr/bin/python3
""" Module with square class """


class Square:
    """
    A class that computes area of a square

    Attributes:
        size: optional, size of the square

    Methods:
        area: returns area of the square
    """
    def __init__(self, size=0):
        """
        Instantaition if the size of the square

        Args:
            size: of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        method to compute area of the square of given size
        """
        return self.__size ** 2
