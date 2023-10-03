#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    for x in range(0, len(str)):
        if x != n:
            new = new + str[x]
    return new
