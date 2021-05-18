#!/usr/bin/python3
'''Class Square'''


class Square():
    '''size validation'''
    def __init__(self, size=0):
        check = isinstance(size, (int))
        if check == False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
