#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
Requirements:
    - You have to manage urllib.error.HTTPError exceptions and print:
            - Error code: followed by the HTTP status code
    - You must use the packages urllib and sys
     -You are not allowed to import other packages than urllib and sys
    - You don’t need to check arguments passed to the script (number or type)
    - You must use the with statement
"""
from sys import argv
from urllib import request, error


def main():
    http_url = argv[1]
    try:
        response = request.urlopen(http_url)
        html = response.read().decode("ascii")
        print(html)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    main()
