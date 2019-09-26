__author__ = 'dev'

# # Dictionaries and sets are unordered
# #
# # Dictionaries are accessed by means of a key, not an index
#
# fruit = {'orange': 'a sweet, orange, citrus fruit',
#          'apple': 'good for making cider',
#          'lemon': 'a sour, yellow, citrus fruit',
#          'grape': 'a small, sweet, fruit growing in bunches',
#          'lime': 'a sour, green, citrus fruit'}
#
# print(fruit)
# print()
# print(fruit['lemon'])
# print()
# print(fruit['apple'])
# print()
#
# # keys in dictionaries must be imutable
# # Here is how you add elements to a dictionary, begining with the key "pear"
# # The key is indicated by the square bracket and the value is set with assignment
# # If we assign a value to an existing key, you effectively replace the key's value, it does not add to the previous
# # value
# fruit["pear"] = "an odd shaped apple"
# print(fruit["pear"])
# print()
# print(fruit)
# # note the new value prints and the old is "lost"
# fruit['lime'] = 'great with tequila'
# print(fruit['lime'])
# print(fruit)
# print()
#
# # Note that even assigning the value in the dictionary twice, to the key, will override the previous assignment.
# # Here I replace apple within the dictionary itself:
# # (ASIDE: IntelliJ/PyCharm gives us a warning that the "dictionary contains duplicate keys 'apple'")
# fruit = {'orange': 'a sweet, orange, citrus fruit',
#          'apple': 'good for making cider',
#          'lemon': 'a sour, yellow, citrus fruit',
#          'grape': 'a small, sweet, fruit growing in bunches',
#          'lime': 'a sour, green, citrus fruit',
#          'apple': 'round and crunchy'}
# # Note that 'round and crunchy' is associated with 'apple' and not 'good for making cider'
# print(fruit)
# print()
# # WARNING: If we fail to identify the key of removal, then we will delete the entire dictionary
# # Now we remove an item from a dictionary using the 'del' command
# del fruit['lemon']
# # Note that 'lemon' is gone
# print(fruit)
# print()
# del fruit
# print(fruit)
# # Instead, we can empty the dictionary with the .clear() method
# fruit.clear()
# print(fruit)
#
# # Try printing a an item that has no assigned key:
# print(fruit['tomato'])
# Key error means a particular key does not exist
# Let's take another stab at it...
# Let's remove the seconds 'apple' entry first
fruit = {'orange': 'a sweet, orange, citrus fruit',
         'apple': 'good for making cider',
         'lemon': 'a sour, yellow, citrus fruit',
         'grape': 'a small, sweet, fruit growing in bunches',
         'lime': 'a sour, green, citrus fruit'}

# while True:
#     dict_key = input(' Please enter a fruit: ')
#     if dict_key == 'quit':
#         break
#     description = fruit.get(dict_key)
#     print(description)
# Note that if a key exists, it will spit out the desired value,
# but if a key does not exist, it will just return 'None' and not error out
#
# Another option is as such:
while True:
    dict_key = input(' Please enter a fruit: ')
    if dict_key == 'quit':
        break
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("We don't have a " + dict_key)
