#!/usr/bin/python3
for c in range(97, 123):
    if chr(c) == 'e' or chr(c) == 'q':
        continue
    else:
        print("{:s}".format(chr(c)), end="")
