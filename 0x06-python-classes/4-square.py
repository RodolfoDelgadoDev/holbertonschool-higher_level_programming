#!/usr/bin/python3
'''Class Square'''


class Square():
    '''size validation'''
    def __init__(self, size=0):
        check = isinstance(size, (int))
        if check is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    '''check area of a square'''
    def area(self):
        self.ar = self.__size ** 2
        return self.ar
    '''def retrive size'''
    @property
    def size(self):
        return self.__size
    '''def setter size'''
    @size.setter
    def size(self, value):
        check = isinstance(value, (int))
        if check is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
