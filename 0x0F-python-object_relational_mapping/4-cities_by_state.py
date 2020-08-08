#!/usr/bin/python3
# Write a script that lists all cities from the database hbtn_0e_4_usa

import sys
import MySQLdb

host = 'localhost'
port = 3306
user = sys.argv[1]
passwd = sys.argv[2]
database = sys.argv[3]

db = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db=database)

cur = db.cursor()

cur.execute("""
    SELECT
        cities.id, cities.name, states.name 
    FROM
        cities, states
    WHERE
        cities.state_id=states.id
    ORDER BY
        cities.id ASC
""")

states = cur.fetchall()

for state in states:
    print(state)
db.close()