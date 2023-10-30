#!/usr/bin/python3
"""print_square - print a square

   Description: print a square according size
   Return: print # with the size square
"""


def print_square(size):
    """print_square - function.
       size - first value.
       second value - Nothing."""
    if type(size) is not int or (type(size) is float and size < 0):
        raise TypeError("size must be an integer")
    if type(size) is int and size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is int and size >= 0:
        for i in range(0, size):
            for j in range(0, size):
                print("#", end="")
            print("", end="\n")
