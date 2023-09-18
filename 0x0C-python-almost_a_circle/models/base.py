#!/usr/bin/python3
""" Module with class Base """

import json


class Base:
    """
    Class that sets value of id

    Attributes:
        __nb_objects: private attribute

    Methods:
        __init__(self, id=None): instantiation of the class attributes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Istantiation method for the class, sets id

        Args:
            id (optional)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON representation of a list of dictionaries """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write JSON string representation of list_objs to a file

        Args:
            cls
            list_objs
        """
        if list_objs is None:
            list_objs = []

        class_name = cls.__name__  # get class name
        filename = class_name + ".json"  # create json file based on class name

        # convert list_objs to a JSON string
        json_data = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs])

        # write the JSON string to the file
        with open(filename, "w") as file:
            file.write(json_data)

    @staticmethod
    def from_json_string(json_string):
        """ Returns list of dictionaries from a JSON string representation """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with attributes set from a dictionary

        Args:
            cls
            dict
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)  # create dummy rectangle
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)  # create dummy square
        else:
            raise ValueError("Unsupported class")

        dummy_instance.update(**dictionary)  # update dictionary values
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Loads instances from a JSON file and returns list of instances
        Args:
            cls
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_str = file.read()
        except FileNotFoundError:
            return []

        json_list = json.loads(json_str)
        instances = [cls.create(**d) for d in json_list]
        return instances
