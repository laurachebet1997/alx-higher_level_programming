#!/usr/bin/python3
'''
script that lists all states from the database
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
        (argv[4],))
    db = cursor.fetchall()
    for i in db:
        print(i)
    cursor.close()
    db.close()
