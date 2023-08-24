#!/usr/bin/python3
"""This script takes an argument and displays all the values
   in the 'states' table from the database 'hbtn_0e_0_usa'
   where 'name' matches the argument
"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])

    c = db.cursor()
    c.execute("SELECT id, name FROM states WHERE\
              name=%s ORDER BY id", (sys.argv[4],))
    allStates = c.fetchall()

    for i in allStates:
        print(i)

    c.close()
    db.close()
