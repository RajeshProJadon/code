# import sqlite3
#
# con = sqlite3.connect("contacts.sqlite")
#
# for row in con.execute("SELECT * FROM contacts"):
#     print(row)
#
# con.close()
# import sqlite3
#
# connt = sqlite3.connect("contacts.sqllite")
#
# name = input("Please enter the name")
# for row in connt.execute("SELECT * FROM contacts where name =?", (name,)):
#     print(row)
#
# connt.close()

import sqlite3
import pytz


db = sqlite3.connect("contacts.sqllite", detect_types=sqlite3.PARSE_DECLTYPES)

for row in db.execute("SELECT * FROM contacts"):
    utc_time = row[0]
    local_time = pytz.utc.localize(utc_time).astimezone()
    print("{}\t{}".format(utc_time, local_time))

db.close()
