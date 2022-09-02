#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    """Returns the square value of all integers of a matrix using map

    Args:
        matrix (list, optional): list of list of integers. Defaults to [].
    """
    return (list(map(lambda x: (list(map(lambda y: y**2, x))), matrix)))
