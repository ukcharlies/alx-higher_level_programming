#!/usr/bin/python3
"""Module containing subclass of BaseGeometry parent class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """SubClass square of the Rectangle class"""

    def __init__(self, size):
        """Initialization of the square class"""
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """
            return area of the square
        """
        return self.__size * self.__size

    def __str__(self):
        """
            string descriptor for rectangle
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
