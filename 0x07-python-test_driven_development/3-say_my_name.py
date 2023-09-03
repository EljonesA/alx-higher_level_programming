#!/usr/bin/python3
"""Prints full name provided first + last name"""

def say_my_name(first_name, last_name=""):
    """The function that implements the printing of full names
    Args:
        first_name: first name
        last_name: last name
    Raises:
        TypeError:
            first name must be a string
            last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")

