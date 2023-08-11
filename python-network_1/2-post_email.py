#!/usr/bin/python3
"""A Python script that takes in a URL
and an email address, sends a POST request
 to the passed URL with the email as a parameter"""

import requests
import sys

def main():
    """The method use to get the URL
    an email"""
    if len(sys.argv) != 3:
        print("Usage: python 2-post_email.py https://intranet.hbtn.io hr@holbertonschool.com")
        return
    
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    response = requests.post(url, data= payload)
    print(response.text)

if __name__ == "__main__":
    main()