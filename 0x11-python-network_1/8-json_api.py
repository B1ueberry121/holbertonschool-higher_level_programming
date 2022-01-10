#!/usr/bin/python3
'''
takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user
with the letter as a parameter
'''
import requests
import sys
if __name__ == '__main__':
    try:
        jsonquery = {"q": sys.argv[1]}
    except:
        jsonquery = {"q": ""}
    url = 'http://0.0.0.0:5000/search_user'
    try:
        req = requests.post(url, jsonquery)
        if (req.json().get('id') is not None):
            print("[{}] {}".format(req.json().get('id'), req.json().get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
