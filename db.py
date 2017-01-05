
import MySQLdb
import sys

#Open dbconnection
try:
    db = MySQLdb.connect(
        host    ="127.0.0.1",
        user    ="root",
        passwd  ="",
        db      ="python"
    )

except Exception as e:
    sys.exit("Database connection error!")

conn = db.cursor()

#conn.execute('''CREATE TABLE user (email VARCHAR(60) PRIMARY KEY, name VARCHAR(60))''')

conn.close()