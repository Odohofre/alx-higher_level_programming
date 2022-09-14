#!/usr/bin/python3
"""
Module 102-square
Defines class Square with private size and public area
Can access and update size
Can be compare with other Node
"""


class Square:
    """class Square definition

    Args:
        size (int): size of a side in square

    Functions:
        __init__(self, size)
        size(self)
        size(self, value)
        area(self)
    """

    def __init__(self, size=0):
        """Initializes square

        Attributes:
            size (int): defaults to 0 if none; don't use __size to call setter
        """
        self.size = size

    def __str__(self):
        """
        Define the print() representation of a Square.
        """
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")

    def __eq__(self, other):
        """
        Compares and returns if equal
        """
        return self.size == other.size

    def __ne__(self, other):
        """
        Compares and returns if not equal
        """
        return self.size != other.size

    def __lt__(self, other):
        """
        Compares and returns if lesser than
        """
        return self.size < other.size

    def __le__(self, other):
        """
        Compares and returns if lesser than or equal to
        """
        return self.size <= other.size

    def __gt__(self, other):
        """
        Compares and returns if greater than
        """
        return self.size > other.size

    def __ge__(self, other):
        """
        Compares and returns if greater than or equal to
        """
        return self.size >= other.size

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
        return (self.__size)**2
