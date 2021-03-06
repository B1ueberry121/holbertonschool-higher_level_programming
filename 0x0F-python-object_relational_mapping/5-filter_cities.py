#!/usr/bin/python3
'''takes a name of a state as an argument and lists all cities'''

import MySQLdb
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    pswd = sys.argv[2]
    dbname = sys.argv[3]
    stateName = sys.argv[4]
    try:
        stateNameP = stateName.split(" ", 1)
    except:
        raise ValueError('Incorrect format')

    db = MySQLdb.connect("localhost", user, pswd, dbname)

    cursor = db.cursor()
    sql = "SELECT DISTINCT cities.name FROM cities INNER JOIN states \
            ON states.id = cities.state_id \
            WHERE states.name LIKE '" + stateNameP[0] + "';"
    str2 = ""
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for item in results:
            for item2 in item:
                str2 += item2 + ", "
        print(str2[:-2])
    except:
        print(sql)
        print("Failed to fetch data")
    db.close()
