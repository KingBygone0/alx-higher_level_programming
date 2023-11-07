#!/usr/bin/python3
""" My class module
"""


class Student:
    """ Student class
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """to_json function"""
        return self

    def to_json(self, attrs=None):
        """to_json with parameters"""
        new_dict = {}
        if attrs is None:
            return self.__dict__
        else:
            for i in attrs:
                if i == "first_name":
                    new_dict.update({'first_name': self.first_name})
                if i == "last_name":
                    new_dict.update({'last_name': self.last_name})
                if i == "age":
                    new_dict.update({'age': self.age})
            return new_dict
