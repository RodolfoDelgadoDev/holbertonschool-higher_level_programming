#!/usr/bin/python3
''' Module '''

''' read file '''


def read_file(filename=""):
    with open(filename, encoding="utf-8") as File:
        File.read()
