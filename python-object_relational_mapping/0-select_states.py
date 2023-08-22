#!/usr/bin/python3
"""A module that list all of the states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


def states(username, password, database):


    """Connect to the MySQL server"""
    db=MySQLdb.connect(host="localhost",
        port=3306, user="mouse",
        passwd="password", db="database")
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
    return db

"""Arguments Usage"""
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    states(username,password,database)