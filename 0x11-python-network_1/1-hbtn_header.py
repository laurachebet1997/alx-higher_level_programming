#!/usr/bin/python3
"""
1-hbtn_header:
    takes in a URL, sends a request to the URL and displays the value of the
    'X-Request-Id' variable found in the header of the response.
Requirements:
    - You must use the packages urllib and sys
    - You are not allow to import packages other than urllib and sys
    - The value of this variable is different for each request
    - You don’t need to check arguments passed to the script (number or type)
    - You must use a with statement
"""
from sys import argv
from urllib import request


def main():
    """
    get response from url
    """
    http_url = argv[1]
    respo = request.urlopen(http_url)
    html = dict(respo.headers).get("X-Request-Id")
    print(html)


if __name__ == "__main__":
    main()
