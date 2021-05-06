#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted(a_dictionary.keys())
    for i in a_dictionary:
        print("{}: {}".format(i, a_dictionary[i]))
