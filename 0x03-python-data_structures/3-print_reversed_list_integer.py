#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    my_list_reversed = my_list[::-1]
    for i in my_list_reversed:
        print("{:d}".format(i))
