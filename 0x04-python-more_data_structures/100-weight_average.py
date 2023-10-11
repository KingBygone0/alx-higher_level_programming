#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        total_weight = sum([t[1] for t in my_list])
        weighted_sum = sum([t[0] * t[1] for t in my_list])
        return weighted_sum / total_weight
