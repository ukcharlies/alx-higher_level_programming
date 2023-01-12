#!/usr/bin/python3
"""Module containing subclass of BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle inheriting from BaseGeometry"""

    def __init__(self, width, height):
        """Initialization of the Rectangle class"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
