#!/usr/bin/python3
''' Function '''


def inherits_from(obj, a_class):
    '''inherits from class'''
    if issubclass(type(obj), a_class) is True and type(obj) is not a_class:
        return True
    else:
        return False
