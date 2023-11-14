#!/usr/bin/python3
""" module point 1 base class """
import json


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string function"""
        if not list_dictionaries or list_dictionaries is None:
            return '[]'
        else:
            new_j = json.dumps(list_dictionaries)
            return new_j

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file function"""
        content = []
        if list_objs is not None:
            for i in range(0, len(list_objs)):
                content += [list_objs[i].to_dictionary()]
        with open(cls.__name__ + ".json", 'w') as f:
            f.write(cls.to_json_string(content))

    @staticmethod
    def from_json_string(json_string):
        """from_json_string function"""
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)
