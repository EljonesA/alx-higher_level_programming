#!/usr/bin/python3
"""A function to print a square using #"""


def print_square(size):
    """
    This function prints a square of size 'size'
    Args:
        size: size of the square to be printed
    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """
    # size must be an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    # size must be greater than 0
    if size < 0:
        raise ValueError("size must be >= 0")
    # size float and less than 0
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
            print('#' * size)
