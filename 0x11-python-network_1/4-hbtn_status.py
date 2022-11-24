#!/usr/bin/python3
"""
4-hbtn_status:
    fetches https://alx-intranet.hbtn.io/status
Requirements:
    - You must use the package requests
    - You are not allowed to import any packages other than requests
    - The body of the response must be displayed like the following
      example (tabulation before -)
"""
import requests


def main():
    """
    get the response
    """
    respo = requests.get('https://alx-intranet.hbtn.io/status')
    respo_content = respo.content
    utf8_content = respo_content.decode("UTF-8")
    respo_type = type(utf8_content)

    print(
            "Body response:\
\n\t- type: {}\
\n\t- content: {}".format(
                        respo_type, utf8_content))


if __name__ == "__main__":
    main()
