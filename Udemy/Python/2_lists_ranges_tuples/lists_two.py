list_1 = []
list_2 = list()     # list constructor

print("List 1: {}".format(list_1))
print("List 2: {}".format(list_2))

if list_1 == list_2:
    print("The lists are equal")

# An iterable is an object which is capable of returning its members one at a time
# All sequence types in python are iterable

print(list("The lists are equal"))

even = [2, 4, 6, 8]
another_even = even
print(another_even is even)     # True because both refer to the same location in memory
another_even.sort(reverse=True)
print(even)                     # This displays [8, 6, 4, 2]
print()
even = [2, 4, 6, 8]
another_even = list(even)       # This is a different
print(even)
print(another_even)
print(another_even is even)     # False because they point to different memory locations
print(another_even == even)     # True because the contests are the same
print()
even = [2, 4, 6, 8]
another_even = sorted()       # This is a different