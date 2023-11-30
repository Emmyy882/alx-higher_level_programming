#!/bin/bash
# gets the size of the body of the response from a URL
curl -sI "$1" | grep -i "content-length" | awk '{print $2}'
