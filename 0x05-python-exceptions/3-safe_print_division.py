#!/usr/bin/python3
def safe_print_division(a, b):
    import sys
    i = 0
    flag = False

    try:
        flag = False
        i = a / b
        return i
    except ZeroDivisionError:
        flag = True
        i = 0
    finally:
        if flag is True:
            print("Inside result: {}".format(None))
        else:
            print("Inside result: {:1.1f}".format(i))
