#!/usr/bin/python3
""" Get dictionary representation for json serialization of an obj """


def class_to_json(obj):
    """
    Get dictionary representation for json serialization of an obj

    Args:
        obj: An instance of a class with serializable attributes

    Returns:
        A dictionary representing the serialized object.
    """
    json_data = {}

    for attr_name, attr_value in obj.__dict__.items():
        if isinstance(attr_value, (list, dict, str, int, bool)):
            json_data[attr_name] = attr_value

    return json_data
