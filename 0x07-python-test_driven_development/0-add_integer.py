#!/usr/bin/python3
"""Add function"""


def add_integer(a, b=98):
    """add function implementation
    Args:
        a: int 1
        b: int 2; optional
    Raises:
       TypeError: a must be an integer
                  b must be an integer
    """
    if not isinstance(a, (int, float)):
        raise ValueError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise  ValueError("b must be an integer")

    # casting flaot a/b into int
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
