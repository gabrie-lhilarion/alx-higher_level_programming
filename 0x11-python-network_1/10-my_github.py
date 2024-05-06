#!/usr/bin/python3
"""
This script takes GitHub credentials
(username and personal access token) and
uses the GitHub API to display your user id.
"""

import requests
import sys


def display_user_id(username, token):
    url = 'https://api.github.com/user'
    headers = {
        'Authorization':
        'Basic '
        + f'{gabdehilas}:{Chisom1984}'.encode('utf-8').decode('utf-8').strip()
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    print("User ID:", data['id'])


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    display_user_id(username, token)
