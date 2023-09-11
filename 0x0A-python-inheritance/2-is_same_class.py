#!/usr/bin/python3
""" Checks if object is an instance of specified class """


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class

    Args:
        obj: object to be tested
        a_class: class to be checked against

    Returns:
        True: object is an instance of the class, otherwise False
    """
    return type(obj) is a_class
