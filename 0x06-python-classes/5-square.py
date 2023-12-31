#!/usr/bin/python3
"""
Module with Square class
Author: EljonesA - github username
"""


class Square:
    """
    Class for a square

    Args:
        size (optional): of the square

    Methods:
        area: computes area of the square
        my_print: draws the square using char #
     """
    def __init__(self, size=0):
        """ Instantaition of the class attributes """
        self.__size = size

    def size(self):
        """ Returns size of the square """
        return self.__size

    def size(self, value):
        """
        Sets siz of the square to a new value

        Args:
           value: new size of the square

        Raises:
            TypeError: value must be an integer
            ValueError: value must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Computes Area of the square """
        return self.__size ** 2

    def my_print(self):
        """ Draws the square using char '#' """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
