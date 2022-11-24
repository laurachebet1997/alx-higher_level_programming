#!/usr/bin/python3
"""
2-post_email:
    takes in a URL and an email, sends a POST request to the passed
    URL with the email as a parameter, and displays the body of the
    response (decoded in utf-8)
Requirements:
    - The email must be sent in the email variable
    - You must use the packages urllib and sys
    - You are not allowed to import packages other than urllib and sys
    - You don’t need to check arguments passed to the script (number or type)
    - You must use the with statement
"""
from sys import argv
from urllib import parse, request


def main():
    """
    post the email to the given address
    """
    http_url = argv[1]
    email = argv[2]
    value = {"email": email}
    data = parse.urlencode(value).encode("ascii")
    respo = request.urlopen(request.Request(http_url, data))
    html = respo.read()
    print(html)


if __name__ == "__main__":
    main()
