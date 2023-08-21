#!/usr/bin/python3

"""A module that lists all of the states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb

def list_states(username, password, database):
    """Connect to the MySQL server"""
    db = MySQLdb.connect(host = "localhost", port = 3306, user = "Gerald", passwd = "password", db = database)
    cursor = db.cursor()
    """Execute the SQL query that fetches all results from the rows"""
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    """Fetch all the rows from the query result"""
    rows = cursor.fetchall()
    """Print the results"""
    for row in rows:
        print(row)
    """Close the cursor"""
    cursor.close()
    """Close the database"""
    db.close()
"""The Usage"""
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
list_states(username, password, database)