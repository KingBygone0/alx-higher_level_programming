#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new = []
    final = []
    rep = 0
    for i in set_1:
        new.append(i)
    for i in set_2:
        new.append(i)
    new.sort()
    for j in range(0, len(new)):
        rep = 0
        for i in range(0, len(new)):
            if new[j] == new[i]:
                rep += 1
        if rep == 1:
            final.append(new[j])
    return final
