#!/usr/bin/python3
""" script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response
(decoded in utf-8) """

import sys
import requests


if __name__ == "__main__":
    ''' Retrieve url & email from command line args '''
    url = sys.argv[1]
    email = sys.argv[2]

    ''' send POST request to url with email as param '''
    response = requests.post(url, data={'email': email})

    print(response.text)
