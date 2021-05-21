#!/usr/bin/python3
'''Function'''


def add_integer(a, b=98):
    '''Def addition between to int'''
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
