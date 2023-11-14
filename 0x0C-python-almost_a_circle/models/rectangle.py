#!/usr/bin/python3
""" module point 2 rectangle class """
from models.base import Base


class Rectangle(Base):
    """class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init function
        width: width
        height: height
        x: x
        y: y
        id: id
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """area function"""
        return self.__height * self.__width

    def display(self):
        """display function"""
        space = ""
        m = 0
        n = 0
        if self.__y > 0:
            for m in range(0, self.__y):
                print("\n", end="")
        if self.__x > 1:
            for n in range(0, self.__x):
                space = space + " "
        if self.__x == 1:
            space = " "
        for i in range(0, self.__height):
            if space != "":
                print(space, end="")
            for j in range(0, self.__width):
                print("#", end="")
            print("\n", end="")

    def __str__(self):
        """str function"""
        return "[{}] ({}) {}/{} - {}/{}\
".format(type(self).__name__, self.id, self.x, self.y,
         self.width, self.height)

    def update(self, *args, **kwargs):
        """update function"""
        if args:
            for i in range(0, len(args)):
                if i == 0:
                    super().__init__(args[i])
                if i == 1:
                    self.width = args[i]
                if i == 2:
                    self.height = args[i]
                if i == 3:
                    self.x = args[i]
                if i == 4:
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
                    super().__init__(value)

    def to_dictionary(self):
        """to_dictionary function"""
        return {'id': self.id, 'width': self.width, 'height\
': self.height, 'x': self.x, 'y': self.y}
