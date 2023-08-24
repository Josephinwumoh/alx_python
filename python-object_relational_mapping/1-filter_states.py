#!/usr/bin/python3
"""A module that lists all states
with a name starting with N (upper N)"""


import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(

            """

            Usage:./1-filter_states.py
            <mysql_username> <mysql_password>
            <database_name>
""")
        sys.exit(1)

    mouse = sys.argv[1]
    password = sys.argv[2]
    hbtn_0e_0_usa = sys.argv[3]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host="localhost",
                             port=3306, user=mouse,
                             passwd=password,
                             db=hbtn_0e_0_usa)
        cursor = db.cursor()

        """Execute the query to retrieve states
        starting with 'N' and order by id"""
        query = """

        SELECT *
        FROM states
        WHERE name LIKE '%\\n'
        ORDER BY id ASC;
        """
        cursor.execute(query)

        # Fetch and display the results
        results = cursor.fetchall()
        for row in results:
            print(row)

        # Close the cursor and the database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)
