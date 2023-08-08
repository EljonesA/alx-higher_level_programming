#!/usr/bin/python3
def uppercase(str):
    string = ""
    for char in str:
        if 'a' <= char <= 'z':
            char_to_upper = chr(ord(char) - ord('a') + ord('A'))
            string += char_to_upper
        else:
            string += char

    return (string)
