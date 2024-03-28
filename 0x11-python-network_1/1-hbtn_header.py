#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL,
and displays the value of the X-Request-Id variable found
in the header of the response.
"""

import urllib.request
import sys


def fetch_x_request_id(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        request_id = response.getheader('X-Request-Id')
        return request_id


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    request_id = fetch_x_request_id(url)
    print(request_id)
