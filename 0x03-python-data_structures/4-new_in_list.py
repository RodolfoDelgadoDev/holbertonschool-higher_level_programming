#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        copy = my_list.copy()
        return copy
    elif idx > len(my_list) - 1:
        copy = my_list.copy()
        return copy
    copy = my_list.copy()
    copy[idx] = element
    return copy
