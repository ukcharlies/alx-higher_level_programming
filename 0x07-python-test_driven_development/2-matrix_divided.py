#!/usr/bin/python3

"""
Module containing function that
divides a matrix.
"""

def matrix_divided(matrix, div):
    """Function to divide a matrix by argument 
    passed to div."""

    if ((not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        for x in row:
            if ((not isinstance(x, int) and not isinstance(x, float))):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    len_rows = []
    for row in matrix:
        len_rows.append(len(row))
    if not all(elem == len_rows[0] for elem in len_rows):
         raise TypeError("Each row of the matrix must have the same size")

    if ((not isinstance(div, int) and not isinstance(div, float))):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return new_matrix
