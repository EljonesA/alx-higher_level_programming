#!/bin/bash
# script that takes in a URL, sends request to that URL, displays body of response
[ "$(curl -sI -w "%{http_code}" "$1" | tail -n1)" -eq 200 ] && curl -s "$1"
