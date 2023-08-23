#!/usr/bin/python3
"""A module that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


"""Connect to the MySQL server"""
if __name__ =="__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    db = MySQLdb.connect(host='localhost',
                         port=3306, user='mouse',
                         passwd='password', 
                         db='hbtn_0e_0_usa')
    cursor= db.cursor()

    """Execute the SQL query"""
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    """fetch all the results"""
    states= cursor.fetchall()

    """print the results"""
    for state in states:
        print(state)

    """Close the database"""
    cursor.close()
    db.close()