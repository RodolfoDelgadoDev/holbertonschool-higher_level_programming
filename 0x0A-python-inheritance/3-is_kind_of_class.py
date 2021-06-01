#!/usr/bin/python3
''' Function '''


def is_kind_of_class(obj, a_class):
    ''' is kind of class '''
    if type(obj) is a_class or issubclass(type(obj), a_class):
        return True
    else:
        return False
