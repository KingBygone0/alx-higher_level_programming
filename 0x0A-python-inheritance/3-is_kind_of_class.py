#!/usr/bin/python3
"""is_kind_of_class - check instance

   Description: return true is same instance
   Return: true or false
"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class - function.
       obj - object.
       a_class."""
    return isinstance(obj, a_class)
