#!/usr/bin/python3
''' Function '''


def inherits_from(obj, a_class):
    '''inherits from class'''
    if issubclass(type(obj), a_class) is True:
        return True
    else:
        return False
