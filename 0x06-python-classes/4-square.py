#!/usr/bin/python
""" Module with square class """


class Square:
    """
    A square class

    Attributes:
        size (optional): of the square

    Methods:
        area: computes the area
    """
    def __init__(self, size=0):
        """
        Instantiation of the class attributes

        Args:
            size (optional): of the square
        """
        self.__size = size

        @size.getter
        def size(self):
            """ Returns size of the square """
            return self.__size

        @size.setter
        def size(self, value):
            """
            Sets size value

            Args:
                value: the value to set size to

            Raises:
                TypeError: size must be an integer
                ValueError: size must be >= 0
            """
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

        def area(self):
            """
            Method to compute the square area

            Returns:
                area
            """
            return self.__size ** 2
