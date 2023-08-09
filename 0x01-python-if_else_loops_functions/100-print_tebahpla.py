#!/usr/bin/python3

start = ord('a')
end = ord('z')

for i in range(end, start - 1, -1):
    letter = chr(i)
    if (ord('z') - i) % 2 == 0:
        print("{}".format(letter.lower()), end='')
    else:
        print("{}".format(letter.upper()), end='')
