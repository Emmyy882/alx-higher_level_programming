#!/usr/bin/python3
"""a script that fetches a url"""
import sys
import urllib.parse
import urllib.request

if __name__ == '__main__':
    url = sys.argv[1]
    value = {'email': sys.argv[2]}

    # encode the data dictionary into a URL-encoded string
    data = urllib.parse.urlencode(value).encode('ascii')
    req = urllib.request.Request(url, data)
    
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print("{}".format(body))
