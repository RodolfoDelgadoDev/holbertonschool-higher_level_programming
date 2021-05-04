#!/usr/bin/python3
def no_c(my_string):
    copy = ""
    for i in range(len(my_string)):
        if my_string[i] != "c" and my_string[i] != "C":
            copy = copy + my_string[i]
    return copy
