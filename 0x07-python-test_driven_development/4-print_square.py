#!/usr/bin/python3

"""
Module containing function to print a square
"""

def print_square(size):
    """Function to print a square"""

    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
