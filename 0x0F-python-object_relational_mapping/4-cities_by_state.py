#!/usr/bin/python3
"""This script lists all 'cities' from the database 'hbtn_0e_4_usa'
"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])

    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name\
              FROM cities\
              INNER JOIN states ON cities.state_id=states.id\
              ORDER BY id")
    citiesByState = c.fetchall()

    for i in citiesByState:
        print(i)

    c.close()
    db.close()
