import db
import sys
conn = db.conn

#conn.execute('''CREATE TABLE user (email VARCHAR(60) PRIMARY KEY, name VARCHAR(60))''')
try:
    conn.execute('''INSERT INTO user (email, name) 
                    VALUES 
                    ('asd@gmail.com','asd'),
                    ('mah@gmail.com','mah')''')
    db.commit()

except Exception as e:
    sys.exit("Database error")

conn.close()