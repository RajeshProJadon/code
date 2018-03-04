import sqlite3

db = sqlite3.connect("address.sqlite")

new_email = "anotherupdate@update.com"
phone = input("Please enter the phone number :")
update_sql = "UPDATE address SET email = '{}' where phone = {}".format(new_email, phone)
print(update_sql)
update_cursor = db.cursor()
update_cursor.execute(update_sql)
print("{} rows updated".format(update_cursor.rowcount))

print()
print("Are connections the same: {}".format(update_cursor.connection == db))
print()

update_cursor.connection.commit()
update_cursor.close()

for name, phone, email in db.execute("select * from address"):
    print(name)
    print(phone)
    print(email)
    print("-" * 20)
db.close()


# for row in db.execute("SELECT * from contacts"):
#     print(row)
#
# db.close()

