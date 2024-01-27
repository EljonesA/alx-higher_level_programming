#!/usr/bin/python3
""" script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response
(decoded in utf-8) """

import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    ''' Retrieve url & email from command line args '''
    url = sys.argv[1]
    email = sys.argv[2]

    ''' encode email '''
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')

    ''' Make post request to url with email as param '''
    with urllib.request.urlopen(url, data) as response:
        body = response.read().decode('utf-8')
        print(body)
