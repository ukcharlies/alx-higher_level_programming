#!/usr/bin/python3
"""Module containing subclass of BaseGeometry parent class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """SubClass Rectangle of the BaseGeometry class"""

    def __init__(self, width, height):
        """Initialization of the rectangle class"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
            return area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
            string descriptor for rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
