#!/usr/bin/python3
''' Module '''


def append_write(filename="", text=""):
    ''' add to the end '''
    with open(filename, mode="a", encoding="utf-8") as File:
        File.write(text)
        c = 0
        for i in text:
            c += 1
        return c
