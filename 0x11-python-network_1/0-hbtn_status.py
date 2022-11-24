#!/usr/bin/python3
"""
0-hbtn_status:
    fetches https://alx-intranet.hbtn.io/status
Requirements:
    - You must use the package urllib
    - You are not allowed to import any packages other than urllib
    - The body of the response must be displayed like the following
      example (tabulation before -)
    - You must use a with statement
"""
from urllib import request


def main():
    """
    get the response
    """
    respo = request.urlopen('https://alx-intranet.hbtn.io/status')
    html = respo.read()
    respo_type = type(html)
    utf8_content = html.decode("UTF-8")
    print(
            "Body response:\
\n\t- type: {}\
\n\t- content: {}\
\n\t- utf8 content: {}".format(
                        respo_type, html, utf8_content))


if __name__ == "__main__":
    main()
