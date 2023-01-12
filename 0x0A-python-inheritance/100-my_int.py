#!/usr/bin/python3

"""Module containing class MyInt which is a subclass
of int"""


class MyInt(int):
    """Invert int operators == to become !=, rebel version of Int object"""

    def __eq__(self, value):
        """returns true if self == value, we are going to invert it"""
        return int(self) != value

    def __ne__(self, value):
        """what was == is now !="""
        return int(self) == value

