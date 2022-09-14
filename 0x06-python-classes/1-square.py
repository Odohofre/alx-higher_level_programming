#!/usr/bin/python3
"""
Module 1-square
Defines class Square with private attribute size
"""


class Square:
    """defines a square

    Args:
        size (int): size of a side in the square

    Functions:
    __init__(self, size)
    """

    def __init__(self, size):
        """Initializes Square

        Args:
            size (int): size of a side of the Square. Defaults to 0.
        """
        self.__size = size
