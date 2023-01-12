#!/usr/bin/python3
"""
Module that defines an inherited list class MyList."""


class MyList(list):
    """Sub-class of parent class list that implements the sorted list"""

    def print_sorted(self):
        """Functiom to print the list"""
        print(sorted(self))
