#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) <= ord('z') and ord(i) >= ord('a'):
            i = chr(ord(i) - 32)
        print("{:s}".format(i), end="")
        print()
