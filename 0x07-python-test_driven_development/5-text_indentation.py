#!/usr/bin/python3
''' Function '''


def text_indentation(text):
    '''function that if in a string there is a . ? or : makes 2 new lines'''
    if type(text) is not str:
        raise TypeError("text must be a string")
    s = ['.', '?', ':']
    c = 0
    for i in range(len(text)):
        if i == 0:
            if text[i] is " ":
                while text[i] == " ":
                    i += 1
                if i == len(text) - 1 and text[i] in s:
                    print(text[i])
                    print()
                    break
                elif i == len(text) - 1:
                    print(text[i], end="")
                    break
                else:
                    print(text[i], end="")
                    continue
        elif text[i] in s:
            print(text[i])
            print()
            i += 1
            while text[i] == " ":
                i += 1
            if i == len(text) - 1 and text[i] in s:
                print(text[i])
                print()
                break
        print(text[i], end="")
