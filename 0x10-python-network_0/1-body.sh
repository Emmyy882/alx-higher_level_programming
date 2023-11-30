#!/bin/bash
# displays the body of the response from a URL
curl -X GET /"$1" HTTP/1.1 | grep -i "Status" | awk '{print $2}' 
