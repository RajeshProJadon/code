# Write a program to append the time tables to our jabberwock poem
# in sample.txt. We want the tables from 2 to 12 (similar to the output
# from the for loops part2 lecture in section 6).
#
# The first column of number shuold be right justified. As an example,
# the 2 times table should look like this:
# 1 times 2 is 2

with open("sample.txt",'a')as tables:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{1:>2} times {0} is {2}".format(i, j, i * j), file=tables)
        print("-" * 20, file=tables)



