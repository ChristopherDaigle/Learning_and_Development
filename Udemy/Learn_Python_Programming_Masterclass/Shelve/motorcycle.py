import shelve

with shelve.open("bike2") as bike:
    # bike["make"] = "Honda"
    # bike["model"] = "250 Dream"
    # bike["color"] = "Red"
# When "engine_size" is mispelled as "engin_size" and the program is run,
# this throws an error because this value DNE, but the file bike2.db
# is still successfully created - that can be an issue
    # bike["engine_size"] = 250
    for key in bike:
        print(key)
    print('='*40)

    del bike['engin_size']

    print(bike["engine_size"])
    # print(bike["engin_size"])
    print(bike["color"])
