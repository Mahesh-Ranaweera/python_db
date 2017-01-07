import db
import sys
import hashlib
conn = db.conn
db   = db.db

def signup_sql(email,FName,LName,Passw1,Passw2):

    #Password hashing
    password1 = raw_input(Passw1)
    password2 = raw_input(Passw2)

    try:
        sql = "INSERT INTO `user`(`email`, `fname`, `lname`, `passw1`, `passw2`) VALUES ('%s','%s','%s','%s','%s')" % \
              (email, FName, LName, password1, password2)
        conn.execute(sql)

        db.commit()
        return True

    except Exception as e:
        sys.exit("Database error")
        #return False

    #conn.close()
