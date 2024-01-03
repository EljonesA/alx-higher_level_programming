#!/bin/bash
# script that takes in a URL, sends request to that URL, returns response size
response_size=$(curl -sI "$1" | grep -i content-length | awk '{print $2}')
