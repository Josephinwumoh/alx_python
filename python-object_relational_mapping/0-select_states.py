#!/usr/bin/python3
"""A module that lists all of the states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <Gerald> <password> <hbtn_0e_0_usa>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        db = MySQLdb.connect(
            host = "localhost",
            port = 3306,
            user = "Gerald",
            passwd = password,
            db = "hbtn_0e_0_usa"
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        states = cursor.fetchall()
        for state in states:
            print(state)
    except MySQLdb.Error as e:
        print("Error connecting to the db:", e)
    finally:
        if db:
            db.close()
