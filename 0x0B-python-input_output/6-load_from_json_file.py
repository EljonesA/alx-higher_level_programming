#!/usr/bin/python3
"""     Creates an object from a JSON file """
import json


def load_from_json_file(filename):
    """
    Creates an objct from a JSON file

    Args:
        filename: file to create obj from
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
