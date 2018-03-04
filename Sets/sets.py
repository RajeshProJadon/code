# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)
#
# for animal in farm_animals:
#     print(animal)
#
# print("=" * 40)
#
# wild_animals = {"Lion", "Tiger", "Elephant", "hare", "panther"}
#
# for animal in wild_animals:
#     print(animal)

# farm_animals.add("horse")
# wild_animals.add("horse")
# print(farm_animals)
# print(wild_animals)

# empty_set = set()
# empty_set.add("a")
# print(empty_set)
#
# even = set(range(0, 40, 2))
# print(even)
# print(len(even))
#
# squares_tuple = {4, 6, 9, 16, 25}
# squares = set(squares_tuple)
# print(squares_tuple)
# print(squares)
# print(len(squares))
#
# print(even.union(squares))
# print(len(even.union(squares)))
#
# print("-" * 40)
#
# print(even.intersection(squares))
# print(len(even.intersection(squares)))

even = set(range(0, 40, 2))
print(sorted(even))
squares_tuple = {4, 6, 9, 16, 25}
squares = set(squares_tuple)
print(sorted(squares))


print("even minus squares")
print(sorted(even.difference(squares)))