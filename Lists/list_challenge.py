# add to program below so that if it finds a meal without spam
# it prints out each of the ingredients of the meal
# you will need to set up the menu as we did in lines 5 - 13
menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "spam", "bacon", "spam"])
menu.append(["egg", "sausage", "spam", "bacon"])
menu.append(["bacon", "spam", "bacon", "spam"])

# print(menu)

for meal in menu:
    if not "spam" in meal:
        print(meal)
        for ingredients in meal:
            print(ingredients)
