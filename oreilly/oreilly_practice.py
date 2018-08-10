def printall(*args):
    print(args)

printall(1, 2, 3)

def sumall(*args):
    add = sum(args)
    print(add)

sumall(23,25,25)

s = 'abc'
t = [0,1,2]
zip(s,t)
for pair in zip(s,t):
    print(pair)

print(list(zip(s,t)))

def has_match(t1, t2):
    for x, y in zip(t1,t2):
        if x == y:
            return True
    return False

print(has_match('8sd123', '8sf126'))

d = {'a':0, 'b':1, 'c':2}
t = d.items()
print(t)

for key, value in d.items():
    print(key, value)



# def line_count(filename):
#     count = 0
#     for line in open(filename):
#         count += 1
#     return count
#
# print(linecount('emma.txt'))