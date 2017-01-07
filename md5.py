
import hashlib

p = input("Enter Password: >>")
hashpass = hashlib.md5(p.encode('utf8')).hexdigest()

#print (hashpass)
