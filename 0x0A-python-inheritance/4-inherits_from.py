#!/usr/bin/python3
"""Function to check is an object is an instance of a class"""


def inherits_from(obj, a_class):
    """Checks if an object is the subclass of a_class.
    Args:
        obj: instnace of class to check
        a_class: class to check
    Return:
        True if its an instnace else False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
