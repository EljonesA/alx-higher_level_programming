#!/usr/bin/python3
""" script that takes your GitHub credentials (username and password) and uses
    the GitHub API to display your id > using Basic authentication
"""

import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'

    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        # Parse the response as JSON
        data = response.json()
        # Display the user id
        print(data.get('id'))
    else:
        print(None)
