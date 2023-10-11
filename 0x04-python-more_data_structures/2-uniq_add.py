#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    my_list.sort()
    for j in range(0, len(my_list)):
        if j != 0 and j < len(my_list) and my_list[j] == my_list[j - 1]:
            continue
        sum += my_list[j]
    return sum
