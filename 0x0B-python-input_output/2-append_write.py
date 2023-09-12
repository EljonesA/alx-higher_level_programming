#!/usr/bin/python3
""" Function that opens and appends data to a file """


def append_write(filename="", text=""):
    """
    Opens a file and appends to it

    Args:
        filename: file to open
        text: data to append to the file

    Returns:
        Number of chars appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        chars_appended = f.write(text)
        return chars_appended
