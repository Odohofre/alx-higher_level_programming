#!/usr/bin/python3
"""
Module 2-rectangle
Defines class Rectangle with:
1. private instance variables; width and height,
2. public methods; area and perimeter
"""


class Rectangle:
    """defines a rectangle

    Args:
       width (int): width of the rectangle
       height (int): height of the rectangle

    Properties:
        __init__(self, width=0, height=0),
        width(self),
        width(self, value),
        height(self),
        height(self, value),
        area(self),
        perimeter(self)
    """

    def __init__(self, width=0, height=0):
        """Initializes the rectangle.

        Args:
            width (int, optional): width of the rectangle, defaults to 0.
            height (int, optional): height of the rectangle, defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """set the value of width

        Args:
            value (int): set width to value if value is int and >= 0

        Raises:
            ValueError: if less than zero
            TypeError: if not an integer

        Return:
            width (int): length of the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set the value of height

        Args:
            value (int): set height to value if value is int and >= 0

        Raises:
            TypeError: if not an integer
            ValueError: if less than zero

        Return:
            height (int): length of the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle
        """
        return self.height * self.width

    def perimeter(self):
        """Returns the perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * (self.height + self.width))
