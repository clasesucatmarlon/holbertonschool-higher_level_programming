#!/usr/bin/python3
"""
script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""
from requests.auth import HTTPBasicAuth
import requests
from sys import argv


def search_api_github():
    """ Search into api github
    """
    """     user = argv[1]
    password = argv[2] """

    """ result = requests.get(
        "https://api.github.com/users/{}".format(argv[1]),
        auth=HTTPBasicAuth(argv[1], argv[2])) """

    """result = requests.get("https://api.github.com/user/",
                          auth=HTTPBasicAuth(argv[1], argv[2]))"""

    result = requests.get('https://api.github.com/user',
                          auth=(argv[1], argv[2]))

    print(result.json().get('id'))


if __name__ == "__main__":
    search_api_github()
