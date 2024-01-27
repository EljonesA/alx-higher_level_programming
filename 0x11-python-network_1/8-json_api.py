#!/usr/bin/python3
""" script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    ''' send post request to url with q as parameter '''
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={'q': q})

    try:
        # parse response as JSON
        data = response.json()

        # check if JSON empty
        if data:
            # not empty
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            # empty JSON
            print("No result")
    except ValueError:
        # invalid JSON
        print("Not a valid JSON")
