#!/usr/bin/python3
"""inherits_from - check sub class

   Description: return true is sub class
   Return: true or false
"""


def inherits_from(obj, a_class):
    """inherits_from - function.
       obj - object.
       a_class."""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
