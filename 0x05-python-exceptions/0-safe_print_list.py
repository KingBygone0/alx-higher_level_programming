#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for 1 in range(x):
            print(my_list[1], end="")
            count += 1
        print()
        return count
    except IndexError:
        print()
        return count
