#!/usr/bin/python3

"""
Module containing class that
defines a rectangle.
"""


class Rectangle:
    """Blueprint that defines a rectangle by width and height"""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the value of the private instance variable width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Function to set the value of width as a  private
        instance attribute
        Args:
            value: value of the width, must be a positive integer
        """

        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """REtrieves value of the private instance variable height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Function to set value of height as a private
        instance attribute
        Args:
            value: value of the height, must be a positive integer
        """
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method that returns the area
        of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Public instance method  that returns the
        perimeter of a rectangle"""
        if self.__width and self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += '#'
            rectangle += '\n'
        return rectangle[:-1]

    def __repr__(self):
        """Return string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = "Rectangle({}, {})".format(self.__width, self.__height)
        return rectangle
