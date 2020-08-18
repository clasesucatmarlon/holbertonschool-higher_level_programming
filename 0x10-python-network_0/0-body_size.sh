#!/bin/bash
# coment
curl -sI "$1" | grep Contenten-Length | cut -d' ' -f2
