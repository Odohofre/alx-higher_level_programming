#!/usr/bin/python3
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
        if size < 0:
            raise ValueError("size must be >= 0")
        elif type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            self.__size = size
