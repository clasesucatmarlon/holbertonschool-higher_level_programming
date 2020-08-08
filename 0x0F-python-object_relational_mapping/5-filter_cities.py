#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""
import sys
import MySQLdb


def filterName():
    """ filter to names
    """
    host = 'localhost'
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    variable = sys.argv[4]

    db = MySQLdb.connect(host=host, port=port, user=user,
                         passwd=passwd, db=database)

    cur = db.cursor()

    cur.execute("""
        SELECT
            cities.name
        FROM
            cities
        WHERE
            cities.state_id=(
                SELECT
                    id
                FROM
                    states
                WHERE
                    name=%s
            )
        ORDER BY
            cities.id ASC
    """, (variable, ))

    cities = cur.fetchall()

    long = len(cities)
    x = 1
    for city in cities:
        if x < long:
            print(city[0], end=", ")
            x += 1
        else:
            print(city[0])

    db.close()


if __name__ == "__main__":
    """ function main
    """
    filterName()
