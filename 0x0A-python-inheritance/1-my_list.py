#!/usr/bin/python3
"""Subclass MyList - inherits from list obj"""


class MyList(list):
    """
    MyList: subclass that inherits from list
    """
    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        sorted_list = sorted(self)
        print(f"{sorted_list}")
