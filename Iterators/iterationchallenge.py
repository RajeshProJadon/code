# Create a list of items (you may use strings or numbers in the list),
# then create an iterator using the iter() function.
#
# use a for loop to loop "n" times, where n is the number of items in your list.
# Each time round the loop, use next() on your list to print the next item.
#
# hint: use the len() function  rather than counting the number of items in the list.

string = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
weekdays = iter(string)

for i in range(0, len(string)):
    next_iter = next(weekdays)
    print(next_iter)

