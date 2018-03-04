import shelve

blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
pasta = ["pasta", "cheese"]

# with shelve.open('recipes') as recipes:
#     recipes["blt"] = blt
#     recipes["beans on toast"] = beans_on_toast
#     recipes["scrambled  eggs"] = scrambled_eggs
#     recipes["soup"] = soup
#     recipes["pasta"] = pasta
#
#     recipes["blt"].append("butter")
#     recipes["pasta"].append("tomato")
#
#     tmp_list = recipes["blt"]
#     tmp_list.append("butter")
#     recipes["blt"] = tmp_list
#
#     tmp_list = recipes["pasta"]
#     tmp_list.append("tomato")
#     recipes["pasta"] = tmp_list

with shelve.open('recipes', writeback=True) as recipes:
    # recipes["soup"].append("croutons")
    # recipes["soup"] = soup
    # recipes.sync()
    # soup.append("cream")

    for snack in recipes:
        print(snack, recipes[snack])