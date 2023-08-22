#!/usr/bin/python3
"""A module that list all of the states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

def list_states(username, password, database):

    """Connect to the MySQL server"""
    db = MySQLdb.connect(host = "localhost", port = 3306, user = "mouse", passwd = "password", db = "hbtn_0e_0_usa")
    cursor = db.cursor()

    """Execute the SQL query"""
    cursor.execute("INSERT INTO states (name) VALUES ("California"), ("Arizona") ORDER BY id ASC")

    """fetch all the results"""
    rows = cursor.fetchall()

    """print the results"""
    for row in rows:
        print(row)

    """Close the database"""
    db.close()
    return db

"""Arguments Usage"""
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

