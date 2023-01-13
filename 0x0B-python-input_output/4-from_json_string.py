#!/usr/bin/python3
"""
Module containing function that decodes objects in
JSON string format into python objects/dict
"""

import json


def from_json_string(my_str):
    """Function to decode a JSON string format object
    and return its python object.
    Args:
        my_str(str): JSON string format to decode
    Returns:
        The python object
    """
    return json.loads(my_str)
