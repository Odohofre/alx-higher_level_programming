#!/usr/bin/python3

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
