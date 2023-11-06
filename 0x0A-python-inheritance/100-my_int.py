#!/usr/bin/python3
"""Module Myint

   Description: change the operator == and !=
   Return: True or False"""


class MyInt(int):
    """MyInt class."""
    def __repr__(self):
        """repr function."""
        return 'False' if self == 1 else 'True'
