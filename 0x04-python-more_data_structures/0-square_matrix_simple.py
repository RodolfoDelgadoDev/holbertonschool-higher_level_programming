#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    cuad = lambda x: x**2
    ma = []
    for i in matrix:
        ma.append(list(map(cuad, i)))
    return ma
