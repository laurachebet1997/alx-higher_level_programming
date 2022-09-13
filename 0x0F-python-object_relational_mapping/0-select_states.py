#!/usr/bin/python3
"""
A script that lists all states from the database hbth_0e_0_usa
"""
if __name__ == "__main__":

    import MySQLdb
    from sys impory argv

    con = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    cursor = con.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    db = cursor.fetchall()
    for i in db:
        print(i)
    cursor.close()
    db.close()
