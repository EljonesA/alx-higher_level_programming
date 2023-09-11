#!/usr/bin/python3
"""Checks if obj is a subclass of a_class """


def inherits_from(obj, a_class):
    """
    Checks if obj is of subclass a_class

    Args:
        obj: the object to check
        a_class: class to check against

    Returns:
        True if issubclass, false otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
