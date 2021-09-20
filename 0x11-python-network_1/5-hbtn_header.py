#!/usr/bin/python3
""" Fetches a URL """
import requests
import sys


if __name__ == "__main__":
    """ Only executes as main """
    r = requests.get(sys.argv[1])
    print(r.headers.get("X-Request-Id"))
