#!/usr/bin/python3
"""Python Network Using Request"""
import requests

req = 'https://alu-intranet.hbtn.io/status'
response = requests.get(req)

print("Body response:")
print(f"\t- type: {type(response.text)}")
print(f"\t- content: {response.text}")




