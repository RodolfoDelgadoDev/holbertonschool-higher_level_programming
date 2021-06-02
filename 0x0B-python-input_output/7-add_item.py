#!/usr/bin/python3
""" class Student """


import json
import os.path
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

myfile = "add_item.json"
if (os.path.isfile(myfile)):
    my_list = load_from_json_file(myfile)
else:
    my_list = []

for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])

save_to_json_file(my_list, myfile)
