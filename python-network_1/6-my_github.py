#!/usr/bin/python3
"""A Python script that takes your
GitHub credentials (username and password)
and uses the GitHub API to display your id"""

import requests
import sys

def main():
    """The method use to get my GitHub credentials
    (username and password)"""
    if len(sys.argv) != 3:
        print("Usage: python 6-my_github.py Josephinwumoh ghp_4gr0uHZxO9y2j")
        return
    username = sys.argv[1]
    token = sys.argv[2]

    url = f"https://api.github.com/user"
    response = requests.get(url, auth=(username, token))
    
    try:
        data = response.json()
        if "id" in data:
            print("id")
        else:
            print("None")

    except ValueError:
        print("Invalid response")

if __name__ == "__main__":
    main()