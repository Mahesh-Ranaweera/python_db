import db
conn = db.conn

conn.execute("SELECT * FROM user")

data = conn.fetchall()

for row in data:
    print "%s, %s" % (row[0], row[1])

conn.close()