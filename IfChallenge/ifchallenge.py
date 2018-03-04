# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be
# over 18 and under 31).
# If they are, welcome them to the holiday, otherwise print
# a (polite) message refusing them entry.

name = input("Please enter your name: ")
age = int(input("How old you are {0}? ".format(name)))

if (age >= 18) and (age <= 30):
    print("Welcome, Mr.{0} Enjoy your holiday".format(name))
else:
    print("Mr.{0}, We are sorry sir you are not eligible for this holiday".format(name))