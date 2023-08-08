#!/usr/bin/python3
start = ord('a')
end = ord('z')

for i in range(start, end + 1):
    if i != ord('e') and i != ord('q'):
        letter = chr(i)
        print("{}".format(letter), end='')
