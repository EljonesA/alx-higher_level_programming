#!/usr/bin/python3

import sys


def command_line_arguments():
    num_of_args = (len(sys.argv) - 1)

# handle first line output
    if num_of_args == 0:
        print("0 arguments.")
    elif num_of_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_of_args))

    if num_of_args > 0:
        i = 1
        for args in sys.argv[1:]:
            print("{}: {}".format(i, args))
            i += 1


if __name__ == "__main__":
    command_line_arguments()
