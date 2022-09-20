#!/usr/bin/python3
"""
Module 9-rectangle
Defines class Rectangle with:
1. private instance variables; width and height,
2. public class variable; number_of_instance, and public_symbol
3. public methods; area and perimeter
4. allows usage of str, repr, and del
5. checks for the bigger rectangle
6. make width and length same
"""


class Rectangle:
    """defines a rectangle

    Args:
       width (int): width of the rectangle
       height (int): height of the rectangle

    Attributes:
        number_of_instances (int): number of instances of object created and
        not deleted
        print_symbol (Any): used in print string representation

    Properties:
        __init__(self, width=0, height=0),
        __str__(self),
        __repr__(self),
        __del__(self),
        width(self),
        width(self, value),
        height(self),
        height(self, value),
        area(self),
        perimeter(self),
        bigger_or_equal(rect_1, rect_2)
        square(cls, size=0)
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the rectangle.

        Args:
            width (int, optional): width of the rectangle, defaults to 0.
            height (int, optional): height of the rectangle, defaults to 0.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """deletes instance of a class"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    def __repr__(self):
        """string representation to recreate a new instance"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __str__(self):
        """print() and str() implementation"""
        if self.width == 0 or self.height == 0:
            return ""
        string = "\n".join([str(self.print_symbol) * self.width
                            for row in range(self.height)])
        return string

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area

        Args:
            rect_1 (Rectangle): first rectangle
            rect_2 (Rectangle): second rectangle
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size

        Args:
        cls: instance class
        size (int, optional): new length for width and height
        """

        return cls(size, size)
