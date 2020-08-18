#!/bin/bash
#  script that takes in a URL, sends a GET request to the URL
curl -s -L -X get "$1"
