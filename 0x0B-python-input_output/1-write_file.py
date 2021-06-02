#!/usr/bin/python3
''' Module '''


def write_file(filename="", text=""):
    ''' write file '''
    with open(filename, mode="w+", encoding="utf-8") as File:
        c = 0
        for i in text:
            c += 1
    return c
