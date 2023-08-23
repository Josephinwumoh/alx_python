#!/usr/bin/python3
"""A module that list all of the states from the database"""
import MySQLdb

"""Connect to the MySQL server"""
db = MySQLdb.connect(host="localhost",
                    port=3306, user="mouse",
                    passwd="password", db="database")
cursor= db.cursor()

cursor.execute("SELECT * FROM states ORDER BY id ASC")
rows= cursor.fetchall()

for row in rows:
    print(row)
