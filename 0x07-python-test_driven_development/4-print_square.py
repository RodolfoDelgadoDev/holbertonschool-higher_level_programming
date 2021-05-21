#!/usr/bin/python3
''' Function '''


def print_square(size):
    ''' function that prints a square '''
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    elif type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size == 0:
        print()
    else:
        area = size ** 2
        cont = 1
        for i in range(1, area + 1):
            if i == size * cont:
                print("#")
                cont += 1
            else:
                print("#", end="")
