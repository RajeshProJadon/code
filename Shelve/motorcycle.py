import shelve

with shelve.open("bike") as bike:
    # bike["bike"] = "Honda"
    # bike["color"] = "red"
    # bike["model"] = "250 dreams"
    # bike["engine_size"] = 250
    for key in bike:
        print(key)

    print("=" * 40)

    print(bike["engine_size"])
    print(bike["color"])
    print(bike["bike"])
