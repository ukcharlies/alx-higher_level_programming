#!/usr/bin/python3
"""
Module containing function that decodes JSON string format
from a file into python objects
"""

import json


def load_from_json_file(filename):
    """Function to decode JSON string format from a file
    into python object.
    Args:
        filename(str): name of file to decode JSON string
        format from.
    """
    with open(filename) as a_file:
        return json.load(a_file)
