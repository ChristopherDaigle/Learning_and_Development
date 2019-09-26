__author__ = 'dev'
#
# # Sets are unordered and able to be repeated, similar to mathematical sets
#
# farmAnimals = {'sheep', 'cow', 'hen'}
# print(farmAnimals)
#
# for animal in farmAnimals:
#     print(animal)
#
# print("=" * 40)
#
# wildAnimals = set(['lion', 'tiger', 'panther', 'elephant', 'hare'])
# print(wildAnimals)
#
# for animal in wildAnimals:
#     print(animal)
# # Add a member to a set
# farmAnimals.add("horse")
# wildAnimals.add("horse")
# print("=" * 40)
#
# print(farmAnimals)
# print(wildAnimals)
# # Note there is no inherent ordering
# emptySet = set()
# emptSet2 = {}
# emptySet.add('a')
# #emptSet2.add('a')
# # Notice that the code on line 29 fails because when the emptySet2 was defined,
# # we didn't define it with the set operator, but with empty curly brackets. Empty
# # curly brackets give us an empty dictionary and as such, dictionaries have no
# # "add" attribute.
# even = set(range(0, 40, 2))
# print(even)
# squaresTuple = (4, 6, 9, 16, 25)
# squares = set(squaresTuple)
# print(squaresTuple)
# print(squares)

# # Unions
# even = set(range(0, 40, 2))
# print(even)
# print(len(even))
# squaresTuple = (4, 6, 9, 16, 25)
# squares = set(squaresTuple)
# print(squares)
# print(len(squares))
#
# print(even.union(squares))
# print(len(even.union(squares)))
# print(squares.union(even))
#
# print("=" * 40)
#
# print(even.intersection(squares))
# # Using the ampersand internally tells python to just use the .intersection method on the arguments
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)
# # We employ the sorted method just for ease of review, it is not necessary for operation

# even = set(range(0, 40, 2))
# print(sorted(even))
# squaresTuple = (4, 6, 9, 16, 25)
# squares = set(squaresTuple)
# print(sorted(squares))
# print("Even minus squares")
# print(sorted(even.difference(squares)))
# print(sorted(even - squares))
#
# print("Squares minus even")
# print(squares.difference(even))
# print(squares - even)
# print("=" * 40)
#
# print(sorted(even))
# print(squares)
# even.difference_update(squares)
# print(sorted(even))
# # Note that now the even set has had the elements from squares removed from it (i.e. 4, 6, and 16 have been removed)

# # Symmetric difference of a set
# even = set(range(0, 40, 2))
# print(even)
# squaresTuple = (4, 6, 9, 16, 25)
# squares = set(squaresTuple)
# print(squares)

# print("Symmetric even minus squares")
# print(sorted(even.symmetric_difference(squares)))
#
# print("Symmetric squares minus even")
# print(sorted(squares.symmetric_difference(even)))
# # The output for both is the same
# # Symmetric difference can be thought of as the opposite of intersection, it's the set of everything EXCEPT
# # the shared values, so everything but 4, 6, and 16 have been returned
# squares.discard(4)
# squares.remove(16)
# squares.discard(8) # no error, does nothing
# print(squares)
# # squares.remove(8) # Will give an error as then umber 8 is not in the set
# # Instead, check this out:
# if 8 in squares:
#     squares.remove(8)
# # You may want to raise an error when removing stuff, so "remove()" is useful for that
# # over "discard()" never throwing an error
# try:
#     squares.remove(8)
# except KeyError:
#     print('The item 8 is not a member of the set')

# even = set(range(0, 40, 2))
# print(even)
# squaresTuple = (4, 6, 16)
# squares = set(squaresTuple)
# print(squares)
# print("=" * 40)
#
# # A set is a subset of another if all its members are contained in the other set
# if squares.issubset(even):
#     print('Squares is a subset of even')
# # A set is a superset of another if it contains all the other set's members
# if even.issuperset(squares):
#     print('Even is a superset of squares')

# Frozen set: immutable set
even = frozenset(range(0, 100, 2))

print(even)
# This won't work, even is a frozenset and is immutable
even.add(3)
