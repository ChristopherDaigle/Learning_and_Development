__author__ = 'dev'

fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow, citrus fruit",
         "grape": "a small, sweet, fruit growing in bunches",
         "lime": "a sour, green, citrus fruit"}
print(fruit)

# fruitKeys = fruit.keys()
# print(fruitKeys)
#
# fruit["tomato"] = "not nice with ice cream"
# print(fruitKeys)
print(fruit.items())
fTuple = tuple(fruit.items())
print(fTuple)
print('-'*40)

for snack in fTuple:
    item, description = snack
    print(item + ' is ' + description)
print('-' * 40)

print(dict(fTuple))
print('-' * 40)
