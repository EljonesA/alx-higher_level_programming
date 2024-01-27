#!/usr/bin/python3
""" Import the urllib package that allows fetching of internet resources """
import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        # read response content
        content = response.read()
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf 8 content: {content.decode('utf-8')}")
