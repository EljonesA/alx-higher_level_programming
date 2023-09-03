#!/usr/bin/python
"""prints text with new lies after special characters"""


def text_indentation(text):
    """
    A function that prints provided text with 2 new lines after special chars

    Args:
        text: the string to be printed

    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    line = ""
    for char in text:
        line += char

        if char in ['.', '?', ':']:
            result += line.strip() + '\n\n'
            line = ""

    if line:
        result += line.strip() + '\n'

    print(result)
