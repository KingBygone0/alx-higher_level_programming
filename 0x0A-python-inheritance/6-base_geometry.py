#!/usr/bin/python3
"""BaseGeometry - module basegeometry class

   Description: class basegeometry
   Return: basegeometry class
"""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """area function."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator function."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name, value))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name, value))
