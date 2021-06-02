#!/usr/bin/python3
''' Module '''


import json


def load_from_json_file(filename):
    ''' load from json file'''
    with open(filename, encoding="utf-8") as File:
        return(json.load(File))
