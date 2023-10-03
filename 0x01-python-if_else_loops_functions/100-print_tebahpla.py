#!/usr/bin/python3
for n in range(122, 96, -1):
    if n % 2 == 0:
        li = n
    else:
        li = n - 32
    print("{:c}".format(li), end="")
