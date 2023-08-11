#!/usr/bin/python3

import sys


def cal():
    if len(sys.argv) <= 1:
        print("0")
    else:
        result = 0
        for args in sys.argv[1:]:
            num = int(args)
            result = result + num
        print(result)


if __name__ == "__main__":
    cal()
