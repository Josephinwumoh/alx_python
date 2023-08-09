#!/usr/bin/python3
"""Response header value"""
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: ./1-hbtn_header.py <https://alu-intranet.hbtn.io/status>")
    sys.exit(1)

req = sys.argv[1]
response = requests.get(req)
x_request_id = response.headers.get('X-Request-Id')
print(x_request_id)