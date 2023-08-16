#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    a function that computes the square value of
    all integers of a matrix
    """

    new_matrix = []

    for row in matrix:
        mat_row = []

        for num in row:
            mat_row.append(num * num)

        new_matrix.append(mat_row)
    return new_matrix
