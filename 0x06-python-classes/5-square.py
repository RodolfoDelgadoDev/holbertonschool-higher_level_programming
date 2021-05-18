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
    '''def my_print'''
    def my_print(self):
        a = self.__size ** 2
        c = 1
        if self.__size == 0:
            print()
        else:
            for i in range(1, a + 1):
                if i == self.__size * c:
                    print("#", end="")
                    print()
                    c += 1
                else:
                    print("#", end="")
