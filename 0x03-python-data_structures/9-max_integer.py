#!/usr/bin/python3
def max_integer(my_list=[]):
    total = 0
    if my_list:
        for i in range(0, len(my_list)):
            for j in range(0, len(my_list)):
                if i != j:
                    if my_list[i] < my_list[j]:
                        total += 1
                    if total == len(my_list) - 1:
                        return my_list[j]
    else:
        return None
