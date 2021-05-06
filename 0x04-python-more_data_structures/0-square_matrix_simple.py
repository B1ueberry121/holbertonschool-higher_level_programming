#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newlist = []
    for idx in range(len(matrix)):
        newlist.append(list(map(lambda idx: idx**2, matrix[idx])))
    return newlist
