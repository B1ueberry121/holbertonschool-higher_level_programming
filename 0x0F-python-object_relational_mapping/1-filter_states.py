#!/usr/bin/python3
''' Lists all states with a name starting with N '''

import MySQLdb
import sys

user = sys.argv[1]
pswd = sys.argv[2]
dbname = sys.argv[3]

db = MySQLdb.connect("localhost", user, pswd, dbname)

cursor = db.cursor()
sql = "SELECT * FROM states WHERE name LIKE 'N%';"
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for item in results:
        print(item)
except:
    print("Failed to fetch data")

db.close()
