#!/usr/bin/python3
"""This script lists all 'states' from the database 'hbtn_0e_0_usa'
"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], host='localhost', port=3306)

    c = db.cursor()
    c.execute("SELECT id, name FROM states ORDER BY id")
    allStates = c.fetchall()

    for i in allStates:
        print(i)

    c.close()
    db.close()
