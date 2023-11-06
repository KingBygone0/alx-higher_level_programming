#!/usr/bin/python3
"""is_same_class - check same class

   Description: return true is same class
   Return: true or false
"""


def is_same_class(obj, a_class):
    """is_same_class - function.
       obj - object.
       a_class."""
    if type(obj) is a_class:
        return True
    else:
        return False
