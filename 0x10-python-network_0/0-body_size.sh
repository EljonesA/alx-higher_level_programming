#!/bin/bash
# script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response

# send request(I option to return only header)
# grep to search for string content-length in response header
# awk to extract 2nd arg from filtered line content-length
url="$1"
response_size=$(curl -sI "$url" | grep -i content-length | awk '{print $2}')
