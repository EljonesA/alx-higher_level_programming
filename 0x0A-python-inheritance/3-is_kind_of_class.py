#!/usr/bin/python3
""" Checks if object is from same class or inherits from a subclass """


def is_kind_of_class(obj, a_class):
    """
    Checks if obj isinstance of a_class or is instance of class that
    a_class inherits from

    Args:
        obj: object to check
        a_class: class to check against

    Returns:
        True if obj isinstance or isinstance of superclss of a_class,
        otherwise False
    """
    return isinstance(obj, a_class)
