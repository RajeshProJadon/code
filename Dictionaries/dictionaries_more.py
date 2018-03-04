fruit ={"Orange": "a sweet, orange, citrus fruit",
        "Apple": "good for making cider",
        "Lemon": "a sour, yellow citrus fruit",
        "Grape": "a small, sweet fruit growing in bunches",
        "Lime": "a sour, green citrus fruit"}

print(fruit)

vegetable = {"cabbage": "every child's favourite",
             "sprouts": "mmmm, lovely",
             "spinach": "can i have some more fruit, please"}

print(vegetable)

vegetable.update(fruit)
print(vegetable)

print(fruit.update(vegetable))
print(fruit)

nice_and_nasty = fruit.copy()
nice_and_nasty.update(vegetable)
print(nice_and_nasty)