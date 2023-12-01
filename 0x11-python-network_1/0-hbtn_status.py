#!/usr/bin/python3
"""a script that fetches a url"""
import urllib.request


if '__name__' == '__main__':
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as\
            response:
        body = response.read()

        print("body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
