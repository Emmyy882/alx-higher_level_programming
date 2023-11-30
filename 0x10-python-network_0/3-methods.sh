#!/bin/bash
# displays all HTTP methods the server will accept
curl -sIX  OPTIONS $1 | grep -i "allow" | awk '{print $2}'
