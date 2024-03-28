#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status using urllib.
"""

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body = response.read()
    print("Body response:")
    print("    - type:", type(body))
    print("    - content:", body)
    print("    - utf8 content:", body.decode('utf-8'))
