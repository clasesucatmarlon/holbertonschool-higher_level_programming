#!/usr/bin/python3
"""
script that takes in a letter and sends a POSTrequest
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
from sys import argv
import requests


def searchapi():
    """ function for search api
    """
    if len(argv) < 2:
        values = ""
    else:
        values = argv[1]

    result = requests.post(
        'http://0.0.0.0:5000/search_user', data={'q': values})

    try:
        data = result.json()
        if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")


if __name__ == "__main__":
    searchapi()
