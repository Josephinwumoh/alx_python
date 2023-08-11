#!/usr/bin/python3
"""A Python script that takes in a URL,
sends a request to the URL and
displays the body of the response."""

import requests
import sys

def main():
    """The method use to get the Error code"""
    if len(sys.argv) != 2:
        print("Usage: python 4-error_code.py https://intranet.hbtn.io")
        return
    
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")

    else:
        print(response.text)

if __name__ == "__main__":
    main()
