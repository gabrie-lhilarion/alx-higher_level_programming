#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL,
and displays the value of the variable X-Request-Id
in the response header.
"""

import requests
import sys


def fetch_x_request_id(url):
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')
    print(request_id)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_x_request_id(url)
