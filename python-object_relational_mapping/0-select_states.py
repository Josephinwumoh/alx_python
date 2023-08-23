import MySQLdb


db = MySQLdb.connect(host="localhost",
                     user="mouse",
                     passwd="password",
                     db="database")

cursor = db.cursor()

cursor.execute("SELECT * FROM rows ORDER BY id ASC")
rows= cursor.fetchall()

for row in rows:
    print(row)
cursor.close()
db.close()
