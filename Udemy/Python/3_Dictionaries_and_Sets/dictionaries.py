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
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("We don't have a {} in fruit".format(dict_key))
