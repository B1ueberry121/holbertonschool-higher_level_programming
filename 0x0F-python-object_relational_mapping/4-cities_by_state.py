#!/usr/bin/python3
''' Lists all cities from database "hbtn_0e_4_usa '''

import MySQLdb
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    pswd = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect("localhost", user, pswd, dbname)

    cursor = db.cursor()
    sql = "SELECT DISTINCT cities.id, cities.name, states.name \
            FROM cities INNER JOIN states ON cities.state_id = states.id;"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for item in results:
            print(item)
    except:
        print(sql)
        print("Failed to fetch data")
    db.close()
