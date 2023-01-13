#!/usr/bin/python3
"""Module containing function that returns the
dictionary description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object:"""


def class_to_json(obj):
    """Function to serialize class instance
    """
    return obj.__dict__
