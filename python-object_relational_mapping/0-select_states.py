import MySQLdb


db = MySQLdb.connect(host="localhost",
                     user="mouse",
                     passwd="password",
                     db="hbtn_0e_0_usa")

cursor = db.cursor()

cursor.execute("SELECT * FROM states ORDER BY id ASC")
rows= cursor.fetchall()

for row in rows:
    print(row)
cursor.close()
db.close()
