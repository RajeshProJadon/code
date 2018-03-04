import sqlite3

connt = sqlite3.connect("contacts.sqllite")

for row in connt.execute("SELECT * FROM contacts"):
    print(row)

connt.close()