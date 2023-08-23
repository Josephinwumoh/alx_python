#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 4:
        print(

            """

            Usage:./1-filter_states.py
            <mysql_username> <mysql_password>
            <database_name>
""")
        sys.exit(1)

    """Get arguments"""

    mouse = sys.argv[1]
    password = sys.argv[2]
    hbtn_0e_0_usa = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306, user=mouse,
                         passwd=password,
                         db=hbtn_0e_0_usa)
    cursor = db.cursor()

    # Query to select states starting with 'N' (case Sensitive)
    query = """

        SELECT *
        FROM states
        WHERE id = %s
        ORDER BY id ASC

    """

    # Execute the query
    cursor.execute(query)

    # Fetch and display the results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the cursor and connection
    cursor.close()
    db.close()
