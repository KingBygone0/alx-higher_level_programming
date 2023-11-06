#!/usr/bin/python3
"""lookup - attributes and method of an object

   Description: return list of attr and methods of an object
   Return: list
"""


def lookup(obj):
    """lookup - function.
       obj - object."""
    return dir(obj)
