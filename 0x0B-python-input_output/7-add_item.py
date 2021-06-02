#!/usr/bin/python3
''' File add item '''


import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

File = 'add_item.json'
if os.path.(File):
    obj = load_from_json_file(File)
else:
    obj = []
for i in range(1, len(sys.argv)):
    obj = obj.append(sys.argv[i])
save_to_json_file(obj, File)
