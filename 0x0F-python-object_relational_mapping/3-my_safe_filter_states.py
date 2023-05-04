#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
This script has been protected from
MySQL injections.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute("SELECT * FROM states \
                    WHERE BINARY name='{:s}' \
                    ORDER BY id ASC".format(argv[4]))

        numrows = cur.fetchall()

    if numrows is not None:
        for item in numrows:
            print(item)