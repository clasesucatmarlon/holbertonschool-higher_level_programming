#!/usr/bin/python3
"""
send post into arg
"""
import urllib.parse
import urllib.request
from sys import argv


def send_mail():
    """ Send mail into arg
    """
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(argv[1], data)

    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode("utf-8"))


if __name__ == "__main__":
    send_mail()
