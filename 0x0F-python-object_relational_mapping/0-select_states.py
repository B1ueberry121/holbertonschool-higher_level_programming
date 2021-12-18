#!/usr/bin/python3
''' Module that lists all states contained in the DB "hbtn_0e_0_usa '''

import MySQLdb
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    pswd = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect("localhost", user, pswd, dbname)

    cursor = db.cursor()
    sql = "SELECT * FROM states;"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for item in results:
            print(item)
    except:
        print("Failed to fetch data")
    db.close()

