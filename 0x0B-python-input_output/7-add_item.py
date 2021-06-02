#!/usr/bin/python3
import sys
import os
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


File = 'add_item.json'
if os.path.exists(File):
    obj = load_from_json_file(File)
else:
    obj = []
for i in range(1, len(sys.argv)):
    obj = obj.append(sys.argv[i])
save_to_json_file(obj, File)
