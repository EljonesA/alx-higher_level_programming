#!/usr/bin/python3


def matrix_divided(matrix, div):
    # check if matrix is a list of lists of integers/floats
    if not all(isinstance(row, list) and all(isinstance(val, (int, float))
        for val in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # check if each row has the same size
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # check if div is either an int/float
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # check if div is equal to zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [] # for storing results list

    for row in matrix:
        new_row = [] # create new row for the result matrix
        for val in row:
            new_val = round(val/div, 2)
            new_row.append(new_val)
        result.append(new_row)

    return result
