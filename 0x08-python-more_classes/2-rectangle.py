#!/usr/bin/python3

"""
This module contains a class Rectangle
"""


class Rectangle:
    """This is an class Rectangle with instance attribute heigth and width"""

    def __init__(self, width=0, height=0):
        """
        initializes height and width of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property getter for the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """
        Property setter for the width
        checks if the type for the width is an integer or < 0
        if above conditions aren't met errors are raised
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Property getter for the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """
        Property setter for the height
        private instance 
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """
        The area of rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        the parimeter of the rectangle
        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self.height)

