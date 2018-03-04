# for i in range(1,20):
#     print("i is now{}".format(i))
#
# number = "9,233,367,15,1987,26,351"
# for i in range(0, len(number)-1):
#     print(number[i])

number = "9,233,367,15,1987,26,351"
for i in range(0, len(number)-1):
    if number[i] in '0123456789':
        print(number[i],end='')
        