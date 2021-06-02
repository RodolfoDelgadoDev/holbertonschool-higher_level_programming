#!/usr/bin/python3
''' Module '''


def read_file(filename=""):
    ''' read file '''
    with open(filename, encoding="utf-8") as File:
        for line in File:
            print(line, end="")
