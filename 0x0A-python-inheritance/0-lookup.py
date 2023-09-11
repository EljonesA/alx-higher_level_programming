#!/usr/bin/python3
"""lookup function"""


def lookup(obj):
    """
    Retrieves a list of attributes and methods of an object

    Args:
        obj (object): the object to inspect

    Returns:
        list: list of attributes and methods.
    """
    attributes_methods = dir(obj)

    return attributes_methods
