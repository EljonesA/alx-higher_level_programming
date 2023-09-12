#!/usr/bin/python3
"""
Adds all arguments to a python list

Args:
    Command line arguments to be added to the list
"""

import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Defining filename for the JSON file
json_filename = "add_item.json"

# empty list to store the items
item_list = []

# check if JSON file exist. if so load its content
if os.path.isfile(json_filename):
    item_list = load_from_json_file(json_filename)

# add cl arg to the list
item_list.extend(sys.argv[1:])

# save the list to a JSON file
save_to_json_file(item_list, json_filename)
