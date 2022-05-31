#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number *= -1
    numberresult = number % 10
    return numberresult
