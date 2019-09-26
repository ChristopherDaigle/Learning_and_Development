__author__ = 'dev'

fruit = {'orange': 'a sweet, orange, citrus fruit',
         'apple': 'good for making cider',
         'lemon': 'a sour, yellow, citrus fruit',
         'grape': 'a small, sweet, fruit growing in bunches',
         'lime': 'a sour, green, citrus fruit'}

print(fruit)

veg = {"cabbage": "every child's favorite",
       "sprouts": "mmmm, lovely",
       "spinach": "can I have some more fruit, please"}

print(veg)
# Updating a dictionary to combine two dictionaries:
veg.update(fruit)
# This adds the fruit and veg dictionary
print(veg)
print('='*40)
# # Note that this does not return a new object
# print(fruit.update(veg)) # prints None
# print(fruit)
print("="*40)

# Create a new dict that contains the other dictionaries, but doesn't modify the originals:
niceAndNasty = fruit.copy()
niceAndNasty.update(veg)
print(niceAndNasty)
print(veg)
print(fruit)
print('='*40)