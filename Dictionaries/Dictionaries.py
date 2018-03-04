fruit ={"Orange": "a sweet, orange, citrus fruit",
        "Apple": "good for making cider",
        "Lemon": "a sour, yellow citrus fruit",
        "Grape": "a small, sweet fruit growing in bunches",
        "Lime": "a sour, green citrus fruit"}

# print(fruit)
# print(fruit["Lemon"])
# fruit["Pear"] = "an odd shaped apple"
# print(fruit)
# fruit["Pear"] = "great with tequila"
# print(fruit)
# del fruit["Lemon"]
# del fruit
# fruit.clear()
# print(fruit)
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "we don't have a " + dict_key)
#     print(description)
#     # if dict_key in fruit:
#     #     description = fruit.get(dict_key)
#     #     print(description)
#     # else:
#     #     print("we don't have a " + dict_key)

print(fruit)

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
# for f in ordered_keys:
#     print(f + "-" + fruit[f])

# fruit_keys = fruit.keys()
# print(fruit_keys)
#
# fruit["tomato"] = "not nice with ice cream"
# print(fruit_keys)
print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

print(dict(f_tuple))
