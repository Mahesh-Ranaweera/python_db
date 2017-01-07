import db
import sys
conn = db.conn

def signin_sql():
    try:
        conn.execute('''INSERT INTO user (email, name) 
                        VALUES 
                        ('asd@gmail.com','asd'),
                        ('mah@gmail.com','mah')''')
        db.commit()
        return True

    except Exception as e:
        sys.exit("Database error")
        return False

    conn.close()
