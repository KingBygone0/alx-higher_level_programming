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


class Rectangle(BaseGeometry):
    """Rectangle class."""

    def __init__(self, width, height):
        """init function."""
        Rectangle.integer_validator(self, "width", width)
        Rectangle.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """str function."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """area function."""
        return self.__width * self.__height


class Square(Rectangle):
    """Square class."""

    def __init__(self, size):
        """init function."""
        Rectangle.integer_validator(self, "size", size)
        self.__size = size

    def __str__(self):
        """str function."""
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """area function."""
        return self.__size ** 2
