__author__ = 'dev'

# for i in range(10):
#     print('i is now {}'.format(i))

# i = 0
# while i < 10:
#     print('i is now {}'.format(i))
#     i +=1

# availableExits = ['east', 'north east', 'south']
#
# chosenExits =''
# while chosenExits not in availableExits:
#     chosenExits = input('Please choose a direction: ')
#     if chosenExits == 'quit':
#         print('Game Over')
#         break
#
# else:
#     print("Aren't you glad you got out of there!")

import random
highest = 10
answer = random.randint(1, highest)

# print('Please guess a number between 1 and {}: '.format(highest))
# if guess != answer:
#     if guess < answer:
#         guess = int(input('Please guess higher: '))
#     else:
#         guess = int(input('Please guess lower: '))
#     if guess == answer:
#         print('Well done! You guessed it!')
#     # else:
#     #     print('Sorry, you have not guessed correctly')
# else:
#     print('You got it on the first try!')

# # My solution:
# guess = int(input('Please guess a number between 1 and {} or enter 0 to exit: '.format(highest)))
# if guess == answer:
#     print('You got it on the first try!')
#
# else:
#     while guess != answer and guess != 0:
#         if guess < answer:
#             guess = int(input('Please guess higher: '))
#         else:
#         else:
#             guess = int(input('Please guess lower: '))
#         if guess == answer:
#             print('Well done! You guessed it!')
#
# if guess == 0:
#     print('Thanks for playing!')

# Tim's Solution
print('Please guess a number between 1 and {}: '.format(highest))
guess = 0
while guess != answer:
    guess = int(input())
    if guess < answer:
        print('Please guess higher: ')
    elif guess > answer:
        print('Please guess lower: ')
    else:
        print('Well done! You guessed it!')
