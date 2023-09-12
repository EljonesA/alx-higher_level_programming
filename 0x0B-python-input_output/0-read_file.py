#!/usr/bin/python3


def read_file(filename=""):
    """
    function that reads and prints data of a file

    Args:
        filename: the file to read from
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
