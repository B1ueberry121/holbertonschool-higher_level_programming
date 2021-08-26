#!/bin/bash
# Takes a URL as an argument
# Sends a GET request to the URL
# Displays the body of the response
curl -s "$1" -H "X-HolbertonSchool-User-Id: 98"
