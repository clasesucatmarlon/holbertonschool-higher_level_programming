#!/usr/bin/python3
"""
check status
"""
import requests
from sys import argv


def post():
    """ status
    """
    r1 = requests.post(argv[1], data={'email': argv[2]})
    print(r1.text)


if __name__ == "__main__":
    post()
