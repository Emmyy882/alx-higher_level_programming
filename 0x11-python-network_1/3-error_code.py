#!/usr/bin/python3
"""a script that fetches a url"""
import sys
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print('{}'.format(body))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
