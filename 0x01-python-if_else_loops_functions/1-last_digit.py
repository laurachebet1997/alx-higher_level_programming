#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
checknumber = 0
if number < 0:
    number *= -1
    checknumber = 1
lastdigit = number % 10
if checknumber == 1:
    number *= -1
    lastdigit *= -1
if lastdigit > 5:
    print(f"Last digit of {number:d} is {lastdigit:d} and is greater than 5")
elif lastdigit == 0:
    print(f"Last digit of {number:d} is {lastdigit:d} and is 0")
else:
    print(f"Last digit of {number:d} is {lastdigit:d} and is less than 6 and not 0")
