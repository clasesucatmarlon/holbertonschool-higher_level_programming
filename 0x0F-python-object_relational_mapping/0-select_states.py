#!/usr/bin/python3
import sys
import MySQLdb


if __name__ == "__main__":
    """ validations numeber of arguments
    """
    if len(argv) != 4:
        print("Syntax: ./0-select_states.py <username> <password> <database name>")
        exit(1)

    host = 'localhost'
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]

    cone = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db=database)

    cur = db.cursor()

    cursor.execute('SELECT * FROM states ORDER BY states.id ASC')

    states = cur.fechall()

    for state in states:
        print(state)
    cur.close()
    db.close()
