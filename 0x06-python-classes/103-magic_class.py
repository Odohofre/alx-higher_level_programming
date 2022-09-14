#!/usr/bin/python3
"""
Module 103-magic_class
Defines class MagicClass with private radius; public area and circumference
"""
import math


class MagicClass:
    """class MagicClass definition

    Args:
        radius (int, float): radius of circle

    Functions:
        __init__(self, radius)
        area(self)
        circumference(self)
    """

    def __init__(self, radius=0):
        """Initializes MagicClass

        Attributes:
            radius (int, float): defaults to 0 if none;
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """calculates area of a circle

        Returns:
            float: area
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """calculates circumference of a circle

        Returns:
            float: circumference
        """
        return 2 * math.pi * self.__radius
