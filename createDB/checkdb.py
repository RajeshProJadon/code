# import sqlite3
#
# con = sqlite3.connect("contacts.sqlite")
#
# for row in con.execute("SELECT * FROM contacts"):
#     print(row)
#
# con.close()
import sqlite3

connt = sqlite3.connect("contacts.sqllite")

name = input("Please enter the name")
for row in connt.execute("SELECT * FROM contacts where name =?", (name,)):
    print(row)

connt.close()