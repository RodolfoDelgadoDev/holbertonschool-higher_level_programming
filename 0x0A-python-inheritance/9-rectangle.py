#!/usr/bin/python3
'''Rectangle'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle'''

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    ''' area '''
    def area(self):
        return self.__width * self.__height

    ''' str '''
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
