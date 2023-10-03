#!/usr/bin/python3
for n in range(0, 10):
    for x in range(0, 10):
        if n < x:
            if n == 8:
                print("{:d}{:d}".format(n, x))
            else:
                print("{:d}{:d}".format(n, x), end=", ")
