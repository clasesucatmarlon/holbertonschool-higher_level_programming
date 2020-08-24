#!/usr/bin/python3
"""
api commit
"""
import requests
from sys import argv


def api_commit():
    """ api commit
    """

    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])

    req = requests.get(url)

    result = req.json()[:10]

    for commi in result:
        sha = commi.get('sha')
        commit = commi.get('commit')
        author = commit.get('author')
        name = author.get('name')
        print("{}: {}".format(sha, name))


if __name__ == "__main__":
    api_commit()
