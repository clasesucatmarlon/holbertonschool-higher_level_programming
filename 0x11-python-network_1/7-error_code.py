#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
and displays the body of the response
"""
from sys import argv
import requests


def codeerror():
    """ function that return code error
    """
    result = requests.get(argv[1])
    if result.status_code > 400:
        print("Error code: {}".format(result.status_code))
    else:
        print(result.text)


if __name__ == "__main__":
    codeerror()
