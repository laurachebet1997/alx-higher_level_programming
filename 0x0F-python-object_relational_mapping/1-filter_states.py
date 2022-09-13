#!/usr/bin/python3
"""
python script that lists all states from the database hbtn_0e_0_usa with a name
starting with N
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("""SELECT states.id, states.name FROM states
                   WHERE states.name LIKE 'N%' ORDER BY states.id ASC""")
    rows = cursor.fetchall()
    for row in rows:
        print(row[0] + ', ' + row[1])
    cursor.close()
    db.close()
