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
        pass #handle any exception without taking action
    finally:
        print() #print new line after all elements
    return count
