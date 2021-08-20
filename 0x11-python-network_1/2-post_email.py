#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request to the passed URL"""
import urllib.request
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    em = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(em).encode()
    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        print(response.read().decode())
