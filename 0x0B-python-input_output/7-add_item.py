#!/usr/bin/python3

"""Script that adds all arguments to a python list
    and then save them to a file
"""


import json
import os.path
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if os.path.isfile('add_item.json'):
    obj = load_from_json_file('add_item.json')

else:
    obj = []
obj.extend(sys.argv[1:])
save_to_json_file(obj, 'add_item.json')
