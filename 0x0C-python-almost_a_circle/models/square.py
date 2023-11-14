#!/usr/bin/python3
""" module point 10 square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """init function
        size: size
        x: x
        y: y
        id: id
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """str function"""
        return "[Square] ({}) {}/{} - {}\
".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """update function"""
        if args:
            for i in range(0, len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.width = args[i]
                    self.height = args[i]
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        if not args:
            for key, value in kwargs.items():
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value

    def to_dictionary(self):
        """to_dictionary function"""
        return {'id': self.id, 'size': self.size, 'x\
': self.x, 'y': self.y}
