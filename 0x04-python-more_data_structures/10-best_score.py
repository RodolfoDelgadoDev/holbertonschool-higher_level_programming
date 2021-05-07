#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        c = 0
        for i in a_dictionary:
            a = a_dictionary.get(i, a_dictionary[i])
            if c < a:
                cc = i
                c = a
        return cc
    else:
        return None
