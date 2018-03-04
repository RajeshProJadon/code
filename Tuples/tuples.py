# t = "a", "b", "c"
# print(t)
#
# print("a", "b", "c")
# print(("a", "b", "c"))

welcome = "welcome to my nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Night flight", "Budgie", 1981
imelda = "More mayhem", "Imelda May", 2011, ((1, "Pulling the Rug"), (2, "Psycho"))




print(imelda)

Title, author, year, tracks = imelda
print(imelda)
print(Title)
print(author)
print(year)
for song in tracks:
    track, title = song
    print("\tTrack number {}, Title: {}".format(track, title))

