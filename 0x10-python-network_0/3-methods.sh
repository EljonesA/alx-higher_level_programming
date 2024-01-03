#!/bin/bash
# script that checks and displays allowed methods of a url
curl -s -i -X OPTIONS "$1" | awk '/Allow:/ {print $2}'
