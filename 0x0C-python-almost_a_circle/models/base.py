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

    def to_json_string(list_dictionaries):
        ''' to json string '''
        return json.dumps(list_dictionaries)
