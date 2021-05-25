#!/usr/bin/python3
''' Functions '''


class Rectangle():
    number_of_instances = 0
    '''class Rectangle'''

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    ''' def retrive width '''

    @property
    def width(self):
        return self.__width

    ''' def setter width '''

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    ''' def retrive height '''

    @property
    def height(self):
        return self.__height

    '''def setter width'''

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    ''' area function '''

    def area(self):
        ar = self.__height * self.__width
        return ar

    ''' perimeter function '''

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        perim = 2 * (self.__height + self.__width)
        return perim

    ''' function that prints '''

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        are = self.__height * self.__width
        cad = ""
        for i in range(self.__height):
            cad = cad + ("#" * self.__width)
            if i != self.__height - 1:
                cad = cad + '\n'
        return cad

    ''' function repr '''

    def __repr__(self):
        sr = "Rectangle({}, {})".format(str(self.width), str(self.height))
        return sr

    ''' function del '''

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
