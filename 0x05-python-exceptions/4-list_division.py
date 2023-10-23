#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    res = 0.0
    flag = 0

    for x in range(0, list_length):
        try:
            flag = 0
            res = 0.0
            res = my_list_1[x] / my_list_2[x]
        except ZeroDivisionError:
            print("division by 0")
            flag = 1
        except TypeError:
            print("wrong type")
            flag = 1
        except IndexError:
            print("out of range")
            flag = 1
        finally:
            if flag is 0:
                new.append(res)
            if flag is 1:
                new.append(0)
    return new
