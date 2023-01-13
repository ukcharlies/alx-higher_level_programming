#!/usr/bin/python3
"""
Module containing function that encodes python objects to
its JSON string format
"""

import json


def save_to_json_file(my_obj, filename):
    """Function to encode python object to JSON string format
    and return its python object.
    Args:
        my_obj(obj): python object to encode
        filename(str): name of file to write JSON string
        format into.
    """
    with open(filename, 'w', encoding='utf-8') as a_file:
        json.dump(my_obj, a_file)
