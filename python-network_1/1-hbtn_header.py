#!/usr/bin/python3
"""A Python script that takes in a URL,
sends a request to the URL and displays
the value of the variable X-Request-Id"""
import requests
import sys

def main():
    """The method use to get the header value"""
    if len(sys.argv) != 2:
        print("Usage: pyton 1-hbtn_header.py https://alu-intranet.hbtn.io/status")
        return
    
    
    url = sys.argv[1]
    response = requests.get(url)

    if "X-Request-Id" in response.headers:
        x_request_id = response.headers.get['X-Request-Id']
        print(x_request_id)

    else:
        print("X-Request-Id not found in response header")

if __name__ == "__main__":
    main()