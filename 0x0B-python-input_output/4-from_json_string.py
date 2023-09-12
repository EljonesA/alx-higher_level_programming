#!/usr/bin/python3
""" Returns Object represented by JSON string """
import json


def from_json_string(my_str):
    """
    Retruns an object represented by a JSON string

    Args:
        my_str: JSON string to return its object

    Returns:
        Object represented by the JSON string
    """
    return json.loads(my_str)
