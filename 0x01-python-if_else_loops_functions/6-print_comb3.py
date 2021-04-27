#!/usr/bin/python3
for i in range(9):
    for j in range(10):
        if i < 1 + j and i != j and (j + i != 17):
            print("{}{}, ".format(i, j), end="")
print("89")
