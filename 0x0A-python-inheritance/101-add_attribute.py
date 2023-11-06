#!/usr/bin/python3
"""module add_attribute

   Description: assign new attribute
   Return: Nothing"""


def add_attribute(obj, field, value):
    """add_attribute -  function
       obj: object
       field: field
       value: value"""
    t = type(obj)
    o = obj
    f = field
    v = value
    if t is not str:
        if t is not int:
            if t is not float:
                if t is not complex:
                    if t is not list:
                        if t is not tuple:
                            if t is not range:
                                if t is not dict:
                                    if t is not set:
                                        if t is not frozenset:
                                            if t is not bool:
                                                if t is not bytes:
                                                    if t is not bytearray:
                                                        if t is not memoryview:
                                                            setattr(o, f, v)
    else:
        raise TypeError("can't add new attribute")
