#!/usr/bin/python3
"""
send request
"""
import urllib.request
import urllib.error
from sys import argv


def sender():
    """ function sender
    """
    try:
        with urllib.request.urlopen(argv[1]) as response:
            the_page = response.read()
            print(the_page.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    sender()
