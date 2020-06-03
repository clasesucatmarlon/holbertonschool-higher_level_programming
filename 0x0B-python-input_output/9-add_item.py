#!/usr/bin/python3
"""add all args
    """


import sys

save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file


try:
    obj = load_from_json_file("add_item.json")
    obj.extend(sys.arg[1:])
    save_to_json_file(obj, "add_item.json")
except FileNotFoundError:
    save_to_json_file(sys.arg[1:], "add_item.json")
