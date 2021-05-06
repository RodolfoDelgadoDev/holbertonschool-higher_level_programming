#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    di = a_dictionary.copy()
    for i in di:
        di[i] = di[i] * 2
    return di
