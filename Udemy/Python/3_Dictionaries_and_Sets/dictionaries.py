fruit = {"orange": "A sweet, orange, citrus fruit",
         "apple": "Good for making cider",
         "lemon": "Sour, yellow, citrus fruit",
         "grape": "Small, sweet fruit growing in bunches",
         "lime": "Sour, green citrus fruit"}
print(fruit)
print(fruit['lemon'])
fruit["pear"] = "an odd shaped apple"
print(fruit)
fruit["lime"] = "great with tequila"
print(fruit)
# Removing an item from the dictionary:
del fruit["lemon"]
print(fruit)
# # Remove all the entries in the dictionary, but maintain the dictionary
fruit.clear()
print(fruit)
fruit = {"orange": "A sweet, orange, citrus fruit",
         "apple": "Good for making cider",
         "lemon": "Sour, yellow, citrus fruit",
         "grape": "Small, sweet fruit growing in bunches",
         "lime": "Sour, green citrus fruit"}

# Issues with accessing non-existent keys:
# print(fruit["tomato"])
while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    description = fruit.get(dict_key, "We don't have a {} in fruit".format(dict_key))
    print(description)
    # if dict_key in fruit:
    #     description = fruit.get(dict_key)
    #     print(description)
    # else:
    #     print("We don't have a {} in fruit".format(dict_key))

for snack in fruit:
    print(fruit[snack])
print()
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#     print(f + " - " + fruit[f])
for f in sorted(fruit.keys()):
    print(f + " - " + fruit[f])
print()
# This method is less efficient than iterating through the keys and printing the values
for val in fruit.values():
    print(val)
print()
# More efficient
for key in fruit:
    print(fruit[key])
print()
# "View objects"
print(fruit.keys())
print(fruit.values())

# Assigning the keys to a variable:
fruit_keys = fruit.keys()
print(fruit_keys)
fruit["tomato"] = "not nice with ice cream"
print(fruit_keys)
