import MySQLdb


db = MySQLdb.connect(host="localhost",
                     user="mouse",
                     passwd="password",
                     db="hbtn_0e_0_usa")

cursor = db.cursor()

cursor.execute("SELECT * FROM rows")
rows= cursor.fetchall()

print(rows)
cursor.close()
db.close()
