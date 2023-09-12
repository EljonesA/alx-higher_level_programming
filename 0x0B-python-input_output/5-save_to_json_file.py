#!/usr/bin/python3
""" Writes an object to a text file using JSON reprsentation """
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an obj to an opened file using JSON representation

    Args:
        my_obj: the object to write to file
        filename: file to write to
    """
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)
