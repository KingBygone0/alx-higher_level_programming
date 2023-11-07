#!/usr/bin/python3
""" Module point 0

    Description: Read a file
    Return: content of a file"""


def read_file(filename=""):
    """read_file function"""
    with open(filename, 'r') as f:
        print(f.read(), end="")
