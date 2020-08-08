#!/usr/bin/python3
"""
List all states with a name staring with N (upper N)
from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


def filter():
    """ filters states with a name staring with N (upper N)
    """
    host = 'localhost'
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host=host, port=port, user=user,
                         passwd=passwd, db=database)

    cur = db.cursor()

    cur.execute('SELECT * FROM states WHERE name LIKE\
                BINARY "N%" ORDER BY states.id ASC')

    states = cur.fetchall()

    for state in states:
        """ if(state[1][0]) == "N": """
        print(state)
    db.close()


if __name__ == "__main__":
    filter()
