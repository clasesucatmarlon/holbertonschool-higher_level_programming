#!/usr/bin/python3
# script that takes in an argument and displays all values in the states table
# of hbtn_0e_0_usa where name matches the argument
import sys
import MySQLdb


def filter():
    """ takes in an argument and displays all values in the states table
    """
    host = 'localhost'
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    name = sys.argv[4]

    db = MySQLdb.connect(host=host, port=port, user=user,
                         passwd=passwd, db=database)

    cur = db.cursor()

    cur.execute('SELECT * FROM states WHERE name = "{}" ORDER BY\
                 states.id ASC'.format(name))

    states = cur.fetchall()

    for state in states:
        print(state)
    db.close()


if __name__ == "__main__":
    filter()
