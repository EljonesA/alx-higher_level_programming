#!/usr/bin/python3
"""Function that writes a string to a text file"""


def write_file(filename="", text=""):
    """
    Opens a file with write mode and writes to it

    Args:
        filename: the file to open
        text: string to write to the opened file

    Returns:
        number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        chars_written = f.write(text)
        return chars_written
