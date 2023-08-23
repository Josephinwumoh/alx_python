import MySQLdb


db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="XmenSound1^100",
                     db="database")

cursor = db.cursor()

cursor.execute("SELECT * FROM states ORDER BY id ASC")
rows= cursor.fetchall()

for row in rows:
    print(row)
cursor.close()
db.close()
