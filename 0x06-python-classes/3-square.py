#!/usr/bin/python3
"""
Module 3-square
Defines class Square with private attribute size and public attribute area
"""


class Square:
    """defines a square

    Args:
        size (int): size of a side in the square

    Functions:
    __init__(self, size=0)
    area(self)
    """

    def __init__(self, size=0):
        """Initializes Square

        Args:
            size (int): size of a side of the Square. Defaults to 0.
        """
        if size < 0:
            raise ValueError("size must be >= 0")
        elif type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            self.__size = size

    def area(self):
        """calculates area of a square

        Returns:
            int: area
        """
        return self.__size * self.__size
