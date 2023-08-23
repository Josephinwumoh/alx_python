#!/usr/bin/python3
"""A module that lists states
    with names starting with N from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


"""Connect to the MySQL server"""
if __name__ == "__main__":
    mouse = sys.argv[1]
    password = sys.argv[2]
    hbtn_0e_0_usa = sys.argv[3]

    """Getting credentials from mysql command arguments"""

    db = MySQLdb.connect(host='localhost',
                         port=3306, user=mouse,
                         passwd=password,
                         db=hbtn_0e_0_usa)

    cursor = db.cursor()
    """Retriving all states queries by id"""
    cursor.execute("SELECT * FROM states ORDER BY id")
    (print (state) for state in cursor.fetchall() if state[1][0] == "N")
     