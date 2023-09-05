#!/usr/bin/python3
"""This script lists all 'cities' from the database 'hbtn_0e_4_usa'
"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])

    c = db.cursor()
    c.execute("SELECT cities.name\
              FROM cities\
              INNER JOIN states ON cities.state_id=states.id\
              WHERE states.name='{}'\
              ORDER BY cities.id".format(sys.argv[4]))
    citiesByState = c.fetchall()

    print(", ".join([i[0] for i in citiesByState]))

    c.close()
    db.close()
