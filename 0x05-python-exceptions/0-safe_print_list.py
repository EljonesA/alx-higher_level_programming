#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for value in my_list:
            if count >= x:
                break
            print(value, end='')
            count += 1
    except:
        pass
    finally:
        print()
    return count
