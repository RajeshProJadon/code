# # for i in range(10):
# #     print("i is now {} ".format(i))
# i = 0
# while i < 10:
#     print("i is now {} ".format(i))
#     i += 1
# available_exits = ["east", "north east", "south"]
# chosen_exit = ""
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")
#     if chosen_exit == "quit":
#         print("Game Over")
#         break
# else:
#     print("aren't you glad to you got out of there!")

import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {} ".format(highest))
guess = int(input())

if guess != answer:
    if guess < answer:
        print("please guess higher")
    else:
        print("please guess lower")
    guess = int(input())
    if guess == answer:
        print("well done you guessed it")
    else:
        print("sorry, you not guess correctly")
else:
    print("you guess it first time")

