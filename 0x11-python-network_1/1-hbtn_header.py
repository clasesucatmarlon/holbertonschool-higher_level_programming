#!/usr/bin/python3
"""
fetcher https://intranet.hbtn.io/status passed into arg
"""
import urllib.request
from sys import argv


def fetcher():
    """ fetcher page into arg
    """
    with urllib.request.urlopen(argv[1]) as response:
        header = response.info()
        print(header['X-Request-Id'])


if __name__ == "__main__":
    fetcher()
