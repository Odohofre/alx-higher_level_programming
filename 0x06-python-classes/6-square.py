#!/usr/bin/python3
"""
Module 6-square
Defines class Square with private size and position; and public area
Can access and update size and position
Can print to stdout the square using #'s
"""


class Square:
    """defines a square

    Args:
        size (int): size of a side in the square

    Functions:
    __init__(self, size=0, position=(0, 0))
    size(self)
    size(self, value)
    position(self)
    position(self, value)
    area(self)
    my_print(self)
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes Square

        Args:
            size (int): size of a side of the Square. Defaults to 0.
            position (tuple): position in the Square. Defaults to (0, 0).
        """
        self.__size = size
        self.__position = position

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
        if value < 0:
            raise ValueError("size must be >= 0")
        elif type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            self.__size = value

    @property
    def position(self):
        """set the value of position

        Args:
            value (int): set position to value if value is tuple of
            two positive ints and >= 0

        Raises:
            TypeError: if less than than zero

        Return:
            tuple: position
        """
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """calculates area of a square

        Returns:
            int: area
        """
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character #
        """
        if self.size == 0:
            print()
        else:
            print("\n" * self.position[1], end="")
            print("\n".join([" " * self.position[0] +
                             "#" * self.size
                             for rows in range(self.size)]))
