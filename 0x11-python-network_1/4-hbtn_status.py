#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status page web
"""
import requests


def status():
    """ function thah status check
    """
    r = requests.get('https://intranet.hbtn.io/status')

    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))


if __name__ == "__main__":
    status()
