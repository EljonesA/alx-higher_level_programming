#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status using request """

import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    response_html = response.text
    print("Body response:")
    print(f"\t- type: {type(response_html)}")
    print(f"\t- content: {response_html}")
