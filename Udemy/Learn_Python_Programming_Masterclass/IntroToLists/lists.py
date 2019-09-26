__author__ = 'dev'

# ipAddress = input('Please enter an IP address')
# print(ipAddress.count('.'))
#
# parrotList = ["not pinin'", "no more", 'a stiff', "bereft of life"]
#
# # Add to the list with .append()
# parrotList.append('A Norwegian Blue')
# for state in parrotList:
#     print('This parrot is ' + state + ".")
#
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# numbers = even + odd
# print(numbers)
#
# numbers.sort()
# print(numbers)
# # sort() method works on the object it's called upon, does not create a new object,
# # so if you print(numbers.sort()), you will receive a none-type
# # HOWEVER! sorted() does return a list which is sorted
# print(numbers.sort())
# print(sorted(numbers))
#
# numbers = even + odd
# numbersInOrder = sorted(numbers)
# print(numbersInOrder)
#
# if numbers == numbersInOrder:
#     print('The lists are equal')
# else:
#     print('The lists are not equal')
#
# if numbersInOrder == sorted(numbers):
#     print('The lists are equal')
# else:
#     print('The lists are not equal')
#
'''Lists constructors'''
# list1 = []
# list2 = list()
#
# print('List 1: {}'.format(list1))
# print('List 2: {}'.format(list2))
#
# if list1 == list2:
#     print('The lists are the same')
#
# print(list('The lists are the same'))

# even = [2, 4, 6, 8]
# # anotherEven = even
# # print(anotherEven is even)
# #
# # x = [1, 2, 3]
# # y = [1, 2, 3]
# # print(x is y)
# #
# # # 'is' IS NOT equal to '=='
# # # '==' checks for values being the same, but 'is' checks for the object being the same (e.g. memory)
# #
# # anotherEven.sort(reverse = True)
# # print(even)
#
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# numbers = [even, odd]
# print(numbers)
#
# for numberSet in numbers:
#     print(numberSet)
#
#     for value in numberSet:
#         print(value)

"""Challenge"""
# Add to the program below so that if it finds a meal without spam
# it prints out each of the ingredients of the meal
# You will need to set up the menu as Tim did in lines 5-13 (I wrote them 83-91)
menu = []
menu.append(['egg', 'spam', 'bacon'])
menu.append(['egg', 'sausage', 'bacon'])
menu.append(['egg', 'spam'])
menu.append(['egg', 'bacon', 'spam'])
menu.append(['egg', 'bacon', 'sausage', 'spam'])
menu.append(['spam', 'bacon', 'sausage', 'spam'])
menu.append(['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'])
menu.append(['spam', 'egg', 'sausage', 'spam'])

# print(menu)

for meal in menu:
    if not 'spam' in meal:
        for ingredient in meal:
            print(ingredient)
