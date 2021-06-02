#!/usr/bin/python3
''' Module '''


class BaseGeometry:
    ''' Class '''
    def area(self):
        ''' area '''
        raise Exception("area() is not implemented")

    ''' integer validator '''
    def integer_validator(self, name, value):
        '''integer validator'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
