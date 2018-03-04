age = int(input("How old are you? "))
 
if (age >=16) and (age<= 65):
    print("Have a good day at work")
 
if 15 < age < 66:
     print("Have a good day at work")
 
if (age < 16) or (age > 65):
    print("Enjoy your free time")
else:
      print("Have a good day at work")

x = input("PLease enter some text ")
if x:
     print("You entered '{}'".format(x))
else:
     print("You did not enter anything")

print(not False)
print(not True)