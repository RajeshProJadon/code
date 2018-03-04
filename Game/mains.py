from player import Player

rajesh = Player("Rajesh")

print(rajesh.name)
print(rajesh.lives)
rajesh.lives -= 1
print(rajesh)

rajesh.lives -= 1
print(rajesh)

rajesh.lives -= 1
print(rajesh)

rajesh.lives -= 1
print(rajesh)

rajesh._lives = 9
print(rajesh)

rajesh.level = 2
print(rajesh)

rajesh.level += 5
print(rajesh)

rajesh.level = 3
print(rajesh)
