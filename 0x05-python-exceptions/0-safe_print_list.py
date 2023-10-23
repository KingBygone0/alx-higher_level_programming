#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    sub = 0

    for j in range(0, x):
        try:
            print(my_list[j], end="")
        except:
            sub = sub - 1
    print("\n", end="")
    return x + sub
