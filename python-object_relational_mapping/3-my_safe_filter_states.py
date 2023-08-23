#!/usr/bin/python3
"""A module that filters and displays values from the states table (safe from SQL injection)"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password> <database name> <state name>".format(sys.argv[0]))
        sys.exit(1)
    
    # Get arguments
    mouse = sys.argv[1]
    password = sys.argv[2]
    hbtn_0e_0_usa = sys.argv[3]
    state_name = sys.argv[4]
    
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host='localhost',
                             port=3306, user=mouse,
                             passwd=password,
                             db=hbtn_0e_0_usa)

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Prepare the SQL query with parameterized input
        query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"

        # Execute the SQL query with the parameter
        cursor.execute(query, (state_name,))

        # Fetch all the rows
        states = cursor.fetchall()

        # Print the results
        for state in states:
            print(state)

        # Close the cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL: {}".format(e))
        sys.exit(1)
