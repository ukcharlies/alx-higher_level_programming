#!/usr/bin/python3
"""
Module containing function that reads a
text file with encoding (UTF-8)
"""


def append_write(filename="", text=""):
    """Function to read a text file and
    print it to stdout
    Args:
        filename(str): file to append text into
        text(str): text to append to file
    Returns: number of characters that was appended
    """
    with open(filename, 'a', encoding='utf-8') as a_file:
        a_file.write(text)
    return len(text)
