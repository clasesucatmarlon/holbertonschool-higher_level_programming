#!/bin/bash
# script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
curl -sH "Content-Type: application/json" --data "@$1" "$2"
