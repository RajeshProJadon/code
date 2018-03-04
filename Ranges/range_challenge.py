# decimals = range(0, 100)
# my_range = decimals[3:40:3]
# print(my_range == range(3, 40, 3))
# print(range(0, 5, 2) == range(0, 6, 2))
# print(list(range(0, 5, 2)))
# print(list(range(0, 6, 2)))
#
#
# r = range(0, 100)
# print(r)
#
# for i in r[::-2]:
#     print(i)
#
#
# print('=' * 50)
# print(range(0, 100)[::-2] == range(99, 0, -2))
#
# for i in range(0, 100, -2):
#     print(i)

# Experiment with different ranges and slices to get a feel for how they work
# Remember that you can print the range as well as iterating through it to print
# its values, to check that your ranges are what you expected.
# you may also want to include things like.
#
o = range(0, 100, 4)
print(o)
p = o[::5]
print(p)
for i in p:
    print(i)

# and see if you can work out will
# be printed before running the program. If you are unsure, use a
# for loop to print out the values of o to see why p returns what it does
