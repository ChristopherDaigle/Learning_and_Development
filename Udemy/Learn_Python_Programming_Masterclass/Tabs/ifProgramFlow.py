# __author__ = 'dev'
# name = input("Enter your name: ")
# age = int(input("How old are you, {0}? ".format(name)))
# print(age)
#
# if age >= 18:
#     print("You are old enough to vote")
#     print("Please put an X in the box.")
# else:
#     print("Please come back in {0} years.".format(18 - age))

# print('Please guess a number between 1 and 10: ')
# guess = int(input())
#
# if guess <5:
#     print('Please guess higher.')
#     guess = int(input())
#     if guess == 5:
#         print('Well done, you guessed it.')
#     else:
#         print('Sorry, you have not guessed correctly.')
# elif guess >5:
#     print('Please guess lower.')
#     guess = int(input())
#     if guess == 5:
#         print('Well done, you guessed it.')
#     else:
#         print('Sorry, you have not guessed correctly.')
# else:
#     print('You got it the first time!')

# print('Please guess a number between 1 and 10: ')
# guess = int(input())
#
# if guess !=5:
#     if guess <5:
#         print('Please guess higher.')
#     else: # guess must be greater than 5
#         print('Please guess lower.')
#
#     guess = int(input())
#     if guess == 5:
#         print('Well done, you guessed it.')
#     else:
#         print('Sorry, you have not guessed corrrectly.')
# else:
#     print('You got it the first try!')

""" More advanced if Elif, Else"""

# age = int(input('How old are you? '))
#
# # if (age>=16) and (age<=65):
# #     print('Have a good day at work!')
# # if 16<= age <= 65:
# #     print('Have a good day at work!')
# # if 15< age < 66:
# #     print('Have a good day at work!')
# if (age < 16) or (age > 65):
#     print('Enjoy your free time')
# else:
#     print('Have a good day at work!')
#
# # if (some_condition) or (some_weird_function()):
#     # do something

# x = 'false'
# if x:
#     print('x is true')

# print(''' False: {0}
# none: {1}
# 0: {2}
# 0.0: {3}
# empty list []: {4}
# empty tuple (): {5}
# empty string '': {6}
# empty string "": {7}
# empty mapping {{}}: {8}
# '''.format(False, bool(None), bool(0), bool(0.0), bool([]), bool(()), bool(''), bool(""), bool({})))

# x = input('Please enter some text: ')
# if x:
#     print('You entered "{}".'.format(x))
# else:
#     print('You did not enter anything.')

# print(not False) # 1
# print(not True) # 0
# age = int(input('How old are you? '))
#
# if not(age < 18):
#     print('You are old enough to vote!')
#     print('Please put an X in the box.')
# else:
#     print('Please come back in {0} years.'.format(18-age))

parrot = 'Norwegian Blue'

letter = input('Enter a character: ')
# if letter in parrot:
#     print('Give me an {}, Bob.'.format(letter))
# else:
#     print('I dont need that letter.')
if letter not in parrot:
    print('I dont need that letter.')
else:
    print('Give me an {}, Bob.'.format(letter))

 