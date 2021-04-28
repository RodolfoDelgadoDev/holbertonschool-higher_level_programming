#!/usr/bin/python3
def print_last_digit(number):
    last = str(number)
    last = last[-1]
    print("{}".format(last), end="")
    return last
