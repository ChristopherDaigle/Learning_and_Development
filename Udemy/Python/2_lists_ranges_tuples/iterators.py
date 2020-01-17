string = "1234567890"

for char in string:
    print(char)
print()

my_iterator = iter(string)
print(my_iterator)          # shows the object's location in memory
print(next(my_iterator))    # shows the first element of the iterator
print(next(my_iterator))    # shows the second element of the iterator
print(next(my_iterator))    # shows the third element of the iterator
print(next(my_iterator))    # shows the fourth element of the iterator
print(next(my_iterator))    # shows the fifth element of the iterator
print(next(my_iterator))    # shows the sixth element of the iterator
print(next(my_iterator))    # shows the seventh element of the iterator
print(next(my_iterator))    # shows the eighth element of the iterator
print(next(my_iterator))    # shows the ninth element of the iterator
print(next(my_iterator))    # shows the tenth element of the iterator
# print(next(my_iterator))    # should break the print
print()

for char in iter(string):
    print(char)
print()

# Create a list of items, then create an iterator using the iter() function
item_list = ['a', 'b', 'c', 'd']
my_iter = iter(item_list)
# Use a for loop to loop "n" times, where n is the number of items in your list
# Each time around the loop, use next() on your list to print the next item
for item in range(len(item_list)):
    print(item, next(my_iter))
