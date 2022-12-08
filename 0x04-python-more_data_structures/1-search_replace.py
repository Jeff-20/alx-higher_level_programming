#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replaced = my_list[:]
    replaced = [x if x != search else replace for x in my_list]
    return (replaced)
