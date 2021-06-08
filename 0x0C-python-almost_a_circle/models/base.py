#!/usr/bin/python3
''' Module '''


import json


class Base:
    ''' Base class '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' init '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    ''' to json string '''

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' to json s '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
