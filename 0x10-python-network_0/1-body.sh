#!/bin/bash
# This script takes in a URL, sends a GET request to the URL, and displays the body of the response for 200 status code responses
curl -sL "$1" -w "%{http_code}" -o /tmp/body_response.txt && [ $(< /tmp/body_response.txt tail -n1) -eq 200 ] && cat /tmp/body_response.txt
