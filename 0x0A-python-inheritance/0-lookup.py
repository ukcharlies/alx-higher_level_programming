#!/usr/bin/python3
"""
Module that contains function
to return all the attributes of an object.
"""


def lookup(obj):
    """Function to return a list of
        an objects attributes(i.e methods
        and fields)
    Args:
        obj: object to lookup
    Return:
        list of the attributes of the object
    """
    return dir(obj)
