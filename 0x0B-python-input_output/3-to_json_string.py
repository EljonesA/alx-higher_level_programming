#!/usr/bin/python3
""" Returns JSON representation of an object """
import json


def to_json_string(my_obj):
    """
    Retruns JSON representation of an object

    Args:
        my_obj: the object to return its JSON representation

    Returns:
        JSON representation
    """
    return json.dumps(my_obj)
