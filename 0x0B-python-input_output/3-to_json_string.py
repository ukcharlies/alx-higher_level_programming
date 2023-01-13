#!/usr/bin/python3
"""
Module containing function that encodes
python objects/dict into its JSON string format
"""

import json


def to_json_string(my_obj):
    """Function to take a python object and return
    its JSON string format
    Args:
        Python object to encode
    Returns:
        The JSON string format
    """
    return json.dumps(my_obj)
