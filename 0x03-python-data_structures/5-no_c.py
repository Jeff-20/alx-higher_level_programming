#!/usr/bin/python3
def no_c(my_string):
    res_str = ""
    for i in range(len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            res_str += my_string[i:(i + 1)]
    return (res_str)
