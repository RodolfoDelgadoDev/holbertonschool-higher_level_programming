#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    dos = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            dos.append(True)
        else:
            dos.append(False)
    return dos
