import sqlite3

db = sqlite3.connect("address.sqlite")
db.execute("create table if not exists address(name text, phone integer, email text)")
db.execute("insert into address(name, phone, email) values('rajesh', 123456, 'rajesh@gmail.com')")
db.execute("insert into address(name, phone, email) values('jadon', 456136, 'update@gmail.com')")
db.execute("insert into address(name, phone, email) values('kumar', 4561378, 'update@gmail.com')")
db.execute("insert into address(name, phone, email) values('Aligrah', 1234, 'update@gmail.com')")


cursor = db.cursor()
cursor.execute("SELECT * FROM address")

# print(cursor.fetchall())
for row in cursor:
    print(row)

cursor.close()
db.close()
