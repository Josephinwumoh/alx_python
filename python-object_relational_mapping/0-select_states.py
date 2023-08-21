#!/usr/bin/env python3
"""
Script to list all states from the hbtn_0e_0_usa database.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=man, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to retrieve states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the results
    results = cursor.fetchall()

    # Display the results
    for row in results:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
