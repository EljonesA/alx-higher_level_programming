#!/usr/bin/python3
"""
Module for Square class
Author: EljonesA - github username
"""


class Square:
    """
    Square class

    Args:
        size (optional): of the square
        position (optional):
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Instatiation of square attributes

        Args:
            size: of the square
            position
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ returns size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets size of the square to new value

        Args:
            value: new size

        Raises:
            TypeError: value must be an int
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter method for position of the square
        Returns position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        sets new position

        Args:
            value: new position

        Raises:
            TypeError:
            ValueError:
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(coord, int) and coord >= 0 for coord in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Method that computes area of the square """
        return self.__size ** 2

    def my_print(self):
        """
        Draws the square using char '#'
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
