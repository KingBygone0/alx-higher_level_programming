#!/usr/bin/python3
"""add_integer - sum of two values

   Description: return messages error if values arent int type and cast to int
   Return: sum of two integers values
"""


def add_integer(a, b=98):
    """add_integer - function.
       a - first value.
       b - second value."""
    if type(a) is not float and type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not float and type(b) is not int:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return int(a + b)
