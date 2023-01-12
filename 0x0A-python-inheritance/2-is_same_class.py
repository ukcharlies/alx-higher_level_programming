#!/usr/bin/python3


"""
Module containing function to check if an object
is an instance of the specified class
"""


def is_same_class(obj, a_class):
    """Function to check if an obj is the instance of a class
    Args:
        obj: instance of class a_class
        a_class: class of obj to check
    Return:
        True if obj is an instance of a_class
        False if otherwise
    """
    if type(obj) == a_class:
        return True
    else:
        return False
