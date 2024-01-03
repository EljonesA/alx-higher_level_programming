#!/bin/bash
# script that checks and displays allowed methods of a url
curl -sI -X OPTIONS "$1" | awk '/Allow:/ {print $2}'
