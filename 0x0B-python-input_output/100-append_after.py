#!/usr/bin/python3
""" Author: Eljones """


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing a specific string file.

    Args:
        filename: name of the file
        search_string: string to search for in each line
        new_string: string to insert after lines containig search_string
    """
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
