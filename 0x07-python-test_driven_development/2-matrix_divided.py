#!/usr/bin/python3
""" Matrix_divided is contains functions to divide a given
    matrix by a given number. """


def matrix_divided(matrix, div):
    """ matrix_divided is a function that received a given matrix
    and a given int/float
    """
    # matrix must be a list of ints and floats
    #  OTHERWISE raise TypeError
    if isinstance(matrix, list):
        for row in matrix:
            if not isinstance(row, list):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            for num in row:
                if not isinstance(num, (int, float)):
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    else:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        
    # each row of the matrix must be the same size
    # OTHERWISE raise TypeError
    for row in matrix:
        if len(row) == len(matrix[0]):
            continue
        else:
            raise TypeError("Each row of the matrix must have the same size")    
    # div must be a number (int/float)
    # OTHERWISE raise TypeError
    # div cannot equal zero
    # OTHERWISE raise ZeroDivisionError
    if isinstance(div, (int, float)):
        if div == 0:
            raise ZeroDivisionError("division by zero")
    else:
        raise TypeError("div must be a number")
    # all elements of matrix should be divided by div
    # format of output should be rounded to 2 dec places
    new_matrix = []
    for row in matrix:
        row = [num / div for num in row]
        new_row = [round(num, 2) for num in row]
        new_matrix.append(new_row)
    # returns a NEW MATRIX
    return new_matrix
