#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements_printed = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end='')
            elements_printed += 1
    except (IndexError, TypeError):
        pass
    print()
    return elements_printed
