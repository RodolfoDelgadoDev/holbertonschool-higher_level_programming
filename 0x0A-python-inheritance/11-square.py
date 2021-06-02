#!/usr/bin/python3
'''Square'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Square'''

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    ''' area '''
    def area(self):
        return self.__size ** 2

    ''' str '''
    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
