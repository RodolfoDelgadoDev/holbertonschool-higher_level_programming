#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, mode="w+", encoding="utf-8") as File:
        c = 0
        for i in text:
            c += 1
    return c
