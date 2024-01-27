#!/usr/bin/python3
"""  script that takes in a URL, sends a request to the URL and displays
     the body of the response (decoded in utf-8).
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    ''' request to url '''
    response = requests.get(url)
    response_html = response.text  # response body
    status_code = response.status_code

    # check if stsatus code >= 400
    if status_code >= 400:
        print(f"Error code: {status_code}")
    else:
        print(response_html)
