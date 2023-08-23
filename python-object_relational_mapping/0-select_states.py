#!/usr/bin/python3
"""A module that list all of the states from the hbtn_0e_0_usa"""
import MySQLdb

"""Connect to the MySQL server"""
db = MySQLdb.connect(host="localhost",
                    port=3306, user="mouse",
                    passwd="password", db="hbtn_0e_0_usa")
cursor= db.cursor()

cursor.execute("SELECT * FROM states ORDER BY id ASC")
rows= cursor.fetchall()

for row in rows:
    print(row)
