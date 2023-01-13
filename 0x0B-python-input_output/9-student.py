#!/usr/bin/python3
"""Module containing class Student"""


class Student():
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes an object of the student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method that returns string dict representation of the object"""
        return self.__dict__
