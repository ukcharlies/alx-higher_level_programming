#!/usr/bin/python3
"""
Module containing function that reads a
text file with encoding (UTF-8)
"""


def read_file(filename=""):
    """Function to read a text file and
    print it to stdout"""

    with open(filename, 'r', encoding='utf-8') as a_file:
        for line in a_file:
            print(line, end="")
