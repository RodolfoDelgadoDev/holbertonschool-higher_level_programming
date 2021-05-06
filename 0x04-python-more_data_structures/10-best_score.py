#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        for i in a_dictionary:
            a = a_dictionary[i]
            a2 = i
            for j in a_dictionary:
                if a < a_dictionary[j]:
                    b = a_dictionary[j]
                    b2 = j
                    break
        if a < b:
            return b2
        else:
            return a2
    else:
        return None
