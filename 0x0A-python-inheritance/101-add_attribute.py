#!/usr/bin/python3
"""Module containing function that adds a new attribute to an object"""


def add_attribute(obj, attribute, value):
    """Function that adds an attribute to an object
    Args:
        obj(any): The object to add an attribute to
        attribute(str): The name of the attribute
        value(any): The value of the attribute
    Raises:
        TypeError: if attribute cant be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
