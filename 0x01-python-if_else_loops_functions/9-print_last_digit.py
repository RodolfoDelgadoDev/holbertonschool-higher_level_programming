#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        num = number * (-1)
        last = num % 10
    else:
        last = number % 10
    print("{}".format(last), end="")
    return last
