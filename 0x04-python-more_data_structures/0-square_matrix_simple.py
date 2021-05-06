#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    ma = []
    for i in matrix:
        ma.append(list(map(cuad=lambda x: x ** 2, i)))
    return ma
