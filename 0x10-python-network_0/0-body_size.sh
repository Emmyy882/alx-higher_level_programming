#!/bin/bash
# gets the size of the body of the response from a URL


# using curl to request and display the size of the body in bytes
curl -sI "$1" | grep -i "content-length" | awk '{print $2}'
