#!/usr/bin/python3
"""script that takes in a letter and sends a POST request"""
import requests
import sys

if __name__ == "__main__":
    if (len(sys.argv) == 2):
        di = {'q': sys.argv[1]}
    else:
        di = {'q': ""}
    r = requests.post('http://0.0.0.0:5000/search_user', data=di)
    if (r.json() == {}):
        print("No result")
    else:
        print("[{}] {}".format(r.json()['id'], r.json()['name']))
