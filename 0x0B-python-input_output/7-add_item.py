#!/usr/bin/python3
''' File add item '''


import json
import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

''' start '''
f = 'add_item.json'
if (os.path.isfile(f)):
    obj = load_from_json_file(f)
else:
    obj = []
for i in range(1, len(sys.argv)):
    obj = obj.append(sys.argv[i])
save_to_json_file(obj, f)
