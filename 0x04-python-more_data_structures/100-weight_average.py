#!/usr/bin/python3
def weight_average(my_list=[]):
    count = 0
    res = 0
    if my_list:
        for (x, y) in my_list:
            res += (x * y)
            count += y
        average = res / count
        return (average)
    else:
        return (0)
