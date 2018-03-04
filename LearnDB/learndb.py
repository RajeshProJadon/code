import sqlite3

conn = sqlite3.connect("address.sqlite")

for row in conn.execute("SELECT * FROM address"):
    print(row)

conn.close()