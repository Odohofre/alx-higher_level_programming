#!/usr/bin/python3
"""
Module 4-square
Defines class Square with private size and public area
Can access and update size
"""


class Square:
    """defines a square

    Args:
        size (int): size of a side in the square

    Functions:
    __init__(self, size=0)
    size(self)
    size(self, value)
    """

    def __init__(self, size=0):
        """Initializes Square

        Args:
            size (int): size of a side of the Square. Defaults to 0.
        """
        self.__size = size

    @property
    def size(self):
        """set the value of size

        Args:
            value (int): set size to value size is int and >= 0

        Raises:
            ValueError: if less than zero
            TypeError: if not an integer

        Return:
            int: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """calculates area of a square

        Returns:
            int: area
        """
        return self.__size ** 2
