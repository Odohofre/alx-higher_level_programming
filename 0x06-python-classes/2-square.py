#!/usr/bin/python3
"""
Module 2-square
Defines class Square with private attribute size and validates size
"""


class Square:
    """defines a square

    Args:
        size (int): size of a side in the square

    Functions:
    __init__(self, size=0)
    """

    def __init__(self, size=0):
        """Initializes Square

        Args:
            size (int): size of a side of the Square. Defaults to 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
