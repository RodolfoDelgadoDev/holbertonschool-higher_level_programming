#!/usr/bin/python3
''' Module '''


import json


def save_to_json_file(my_obj, filename):
    ''' save to json file '''
    with open(filename, mode="w+", encoding="utf-8") as File:
        json.dump(my_obj, File)
