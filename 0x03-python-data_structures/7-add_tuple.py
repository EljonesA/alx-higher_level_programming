#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2:
        a1, a2 = tuple_a[:2]
    elif len(tuple_a) == 1:
        a1, a2 = tuple_a[0], 0
    else:
        a1, a2 = 0, 0

    if len(tuple_b) >= 2:
        b1, b2 = tuple_b[:2]
    elif len(tuple_b) == 1:
        b1, b2 = tuple_b[0], 0
    else:
        b1, b2 = 0, 0

    resulting_tuple = (a1 + b1, a2 + b2)
    return resulting_tuple
