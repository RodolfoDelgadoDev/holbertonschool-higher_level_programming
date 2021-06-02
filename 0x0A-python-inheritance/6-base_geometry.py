#!/usr/bin/python3
''' Classes '''


class BaseGeometry:
    ''' Base geometry '''
    def area(self):
        raise Exception("area() is not implemented")
