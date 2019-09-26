__author__ = 'dev'

fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow, citrus fruit",
         "grape": "a small, sweet, fruit growing in bunches",
         "lime": "a sour, green, citrus fruit"}

# The way this dictionary works is a 'hash' in that it will not necessarily return the same order each time
# ASIDE: mine seems to return the same order each time, for whatever reason, but it's worth being aware that
# the dictionary is unordered
# NOTE: Dictionaries are refered to as hashes
print(fruit)
#
# while True:
#     dKey = input(' Please enter a fruit: ')
#     if dKey == 'quit':
#         break
#     description = fruit.get(dKey, "We don't have a " + dKey)
#     # this is deprecated from Python2
#     # description.has_key(dKey)
#     print(description)
#     # if dKey in fruit:
#     #     description = fruit.get(dKey)
#     #     print(description)
#     # else:
#     #     print("We don't have a " + dKey)
# Now when we type, if the key is in the dictionary, we get the value,
# but if the value is not, we get the alternative print statement of "We don't..."

# for snack in fruit:
#     print(fruit[snack])

# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print('-' * 40)

orderedKeys = list(fruit.keys())
orderedKeys.sort()
# More succinct method...
orderedKeys = sorted(list(fruit.keys()))
for f in orderedKeys:
    print(f + " - " + fruit[f])
# Even MORE succint method!:
for f in sorted(fruit.keys()):
    print(f + " - " + fruit[f])
for val in fruit.values():
    print(val)

print('-' * 40)

for key in fruit:
    print(fruit[key])

