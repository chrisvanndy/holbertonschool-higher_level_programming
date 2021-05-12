#!/usr/bin/python3
"""Module creates method add_item which adds all arguments to a\
Python list, and saves the list to a file"""

# import sys to handle command line args (sys.argv[])
import sys

# import json to handle json syntax in imported functions
import json

# save_to_json_file takes python object and dumps
# the object to json string via write()
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

# load_from_json_file creates a python object
# from a file with json representation (str)
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    theList = load_from_json_file("add_item.json")

except:
    theList = []

for i in range(1, len(sys.argv)):
    theList.append(sys.argv[i])

save_to_json_file(theList, "add_item.json")
