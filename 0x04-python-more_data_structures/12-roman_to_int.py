#!/usr/bin/python3
def roman(i):
    switcher = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
         }
    return switcher.get(i, 0)


def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    new = []
    total = 0
    flag = 0
    for i in roman_string:
        if i.isdigit() is True:
            return 0
        if i == 'I' or i == 'V' or i == 'X' or i == 'L\
' or i == 'C' or i == 'D' or i == 'M':
            new.append(roman(i))
        else:
            return 0
    for i in range(0, len(new)):
        flag = 0
        if i < (len(new) - 1):
            if (new[i + 1] == 5 or new[i + 1] == 10 and flag == 0):
                if new[i] == 1 and new[i] < new[i + 1]:
                    total += new[i] * -1
                    flag = 1
            if new[i + 1] == 50 or new[i + 1] == 100 and flag == 0:
                if new[i] == 10 and new[i] < new[i + 1]:
                    total += new[i] * -1
                    flag = 1
            if new[i + 1] == 500 or new[i + 1] == 1000 and flag == 0:
                if new[i] == 100 and new[i] < new[i + 1]:
                    total += new[i] * -1
                    flag = 1
            if flag == 0:
                total += new[i]
        else:
            total += new[i]
    return total
