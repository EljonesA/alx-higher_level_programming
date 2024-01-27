#!/usr/bin/python3

"""  script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""
import requests
import sys


if __name__ == "__main__":
    ''' capture command line arg url '''
    url = sys.argv[1]

    ''' GET request to the url & get value of X-Request-Id variable '''
    response = requests.get(url)

    # get value of variable from resposne header
    x_request_id = response.headers.get('X-Request-Id')

    print(x_request_id)
