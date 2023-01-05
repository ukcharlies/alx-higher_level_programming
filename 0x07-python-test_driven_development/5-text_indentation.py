#!/usr/bin/python3


"""
Module containing function to
indent text, passed into the function by adding
2 new lines after each of these characters(. ? :)
"""


def text_indentation(text):
    """Function to indent text"""

    if (not isinstance(text, str)):
        raise TypeError("text must be a string")

    for delim in ".?:":
        text = (delim + '\n\n').join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
