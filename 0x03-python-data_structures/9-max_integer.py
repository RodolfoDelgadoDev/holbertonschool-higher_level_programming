#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) > 0:
        a = my_list[0]
        if len(my_list) == 1:
            return a
        for i in range(1, len(my_list)):
            if my_list[i] > a:
                a = my_list[i]
        return a
    else:
        return None
