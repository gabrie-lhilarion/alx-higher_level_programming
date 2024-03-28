#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status
using the requests package.
"""

import requests


def fetch_status():
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    print("Body response:")
    print("    - type:", type(response.text))
    print("    - content:", response.text)


if __name__ == "__main__":
    fetch_status()
