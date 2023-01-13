#!/usr/bin/python3
"""Module containing class Student"""


class Student():
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes an object of the student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method that returns string dict representation of the object"""
        if isinstance(attrs, list) and all(
                isinstance(s, str) for s in attrs):
            return {el: getattr(self, el) for el in attrs if hasattr(self, el)}
        return self.__dict__
