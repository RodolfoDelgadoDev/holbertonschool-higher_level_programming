#!/usr/bin/python3
''' Module '''


class Student:
    '''Student init'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    ''' to json '''
    def to_json(self, attrs=None):
        dic = {}
        if type(attrs) is list:
            for i in attrs:
                if type(i) is not str:
                    return (self.__dict__)
            for j in attrs:
                if j in self.__dict__:
                    dic[j] = self.__dict__[j]
            return dic
        return (self.__dict__)
