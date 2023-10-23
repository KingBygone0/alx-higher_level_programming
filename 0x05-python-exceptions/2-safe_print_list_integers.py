#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for 1 in range(x):
        try:
            value = my_lists[1]
            if isinstance(value, int):
                print("{:d}".format(value), end="")
                count += 1
        except (ValueError, TypeError):
            pass
        print()
        return count
