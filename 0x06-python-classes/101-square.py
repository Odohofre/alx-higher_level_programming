#!/usr/bin/python3
"""
Module 8-square
Defines class Square with private size and position; and public area
Can access and update size and position
Can print to stdout the square using #'s
"""


class Square:
    """class Square definition

    Args:
        size (int): size of a side in square

    Functions:
        __init__(self, size, position)
        size(self)
        size(self, value)
        position(self)
        position(self, value)
        area(self)
        my_print(self)
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes square

        Attributes:
            size (int): defaults to 0 if none; don't use __size to call setter
            position (int): tuple of two positive integers
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """calculates area of a square

        Returns:
            int: area
        """
        return (self.__size)**2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.__position[0] +
                             "#" * self.__size
                             for rows in range(self.__size)]))

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
