#!/usr/bin/python3
"""A module that lists cities of a specific state from the database hbtn_0e_4_usa"""

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
    hbtn_0e_4_usa = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host='localhost',
                             port=3306, user=mouse,
                             passwd=password,
                             db=hbtn_0e_4_usa)

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Prepare the SQL query with parameterized input
        query = """SELECT cities.name
                   FROM cities
                   INNER JOIN states ON cities.state_id = states.id
                   WHERE states.name = %s
                   ORDER BY cities.id ASC"""

        # Execute the SQL query with the parameter
        cursor.execute(query, (state_name,))

        # Fetch all the rows
        cities = cursor.fetchall()

        # Print the results
        cities_list = [city[0] for city in cities]
        print(", ".join(cities_list))

        # Close the cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL: {}".format(e))
        sys.exit(1)
