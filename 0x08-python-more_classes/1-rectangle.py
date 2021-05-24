#!/usr/bin/python3
''' Functions '''


class Rectangle:
    '''class Rectangle'''

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    ''' def retrive width '''

    @property
    def width(self):
        return self.__width

    ''' def retrive height '''

    @property
    def height(self):
        return self.__height

    ''' def setter width '''

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    '''def setter height'''

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
