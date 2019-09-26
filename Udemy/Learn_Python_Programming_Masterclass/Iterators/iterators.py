__author__ = 'dev'

string = '1234567890'

# for char in string:
#     print(char)

# myIter = iter(string)
# print(myIter)
# # 1
# print(next(myIter))
# # 2
# print(next(myIter))
# # 3
# print(next(myIter))
# # 4
# print(next(myIter))
# # 5
# print(next(myIter))
# # 6
# print(next(myIter))
# # 7
# print(next(myIter))
# # 8
# print(next(myIter))
# # 9
# print(next(myIter))
# # 0
# print(next(myIter))
# # Next one won't work
# print(next(myIter))
#
# # This is what a for loop does and ceases when it gets "stop iteration error"
#
# # This implicitly creates an iterable from the string
# for char in string:
#     print(char)
# print()
#
# # This one has an iterator explictly defined so the for loop itself is not creating this
# for char in iter(string):
#     print(char)
"""Challenge
Create a list of items (you may use either strings or numbers in the list),
then create an iterator using the iter() function.

Use a for loop to loop "n" times, where n is the number of items in your list.
Each time round the loop, use next() on your list to print the next item.

hint: use the len() function rather than counting the number of items in the list
"""
# My solution
itemList = ['a1', 'b2', 'c3', 'd4', 'e5', 'f6', 'g7']

iterList = iter(itemList)

for i in range(len(itemList)):
    print(next(iterList))
print()

for i in itemList:
    print(i)
