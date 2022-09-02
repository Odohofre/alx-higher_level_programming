#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Returns the square value of all integers of a matrix.

    Args:
        matrix (list, optional): matrix. Defaults to [].
    """
    new_matrix = [[col * col for col in row] for row in matrix]
    return new_matrix
