import db
import sys
conn = db.conn
db = db.db

email = "mi6softlab@gmail.com"
FName = "Mahesh"
LName = "Ranaweera"
#password1 = raw_input("123")
#password2 = raw_input("123")


password1 = "123"
password2 = "123"

try:
    sql = "INSERT INTO `user`(`email`, `fname`, `lname`, `passw1`, `passw2`) VALUES ('%s','%s','%s','%s','%s')" % \
          (email, FName, LName, password1, password2)
    conn.execute(sql)

    db.commit()
    print "DONE"

except Exception as e:
    sys.exit("Database error")

conn.close()
