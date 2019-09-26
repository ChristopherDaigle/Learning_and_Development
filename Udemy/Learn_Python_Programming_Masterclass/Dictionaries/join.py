__author__ = 'dev'

# myList = ['a', 'b', 'c', 'd']
#
# ## Highly inefficient as every loop makes a completely new strong nd is computationally taxing
# ## So, we have another option for this sort of thing known as the join method
# # newString = ''
# # for c in myList:
# #     newString += c + ", "
# # print(newString)
# #
# # Using the join() method
# newString = ", ".join(myList)
# print(newString)
# print('-' * 40)
#
# letters = 'abcdefghijklmnopqrstuvwxyz'
# newString = ', '.join(letters)
# print(newString)
# print('-' * 40)
#
# numbers = '1234567890'
# newString = ' mississippi, '.join(numbers)
# print(newString)
# print('-' * 40)

# Concatenating the keys of a dictionary to give us a string
#
# Here's a dictionary that stores locations and allows a 'player' to select this map
locations = {0: 'You are sitting in front of a computer learning Python',
             1: 'You are standing at the end of a road before a small brick building',
             2: 'You are at the top of a hill',
             3: 'You are inside a building, a well house for a small stream',
             4: 'You are in a valley beside a stream',
             5: 'You are in the forest'}
# Desired available exits: N, S, E, W, + 'quit' to exit the game
exits = [{'Q': 0},
         {'W': 2, 'E': 3, 'N': 5, 'S': 4, 'Q': 0},
         {'N': 5, 'Q': 0},
         {'W': 1, 'Q': 0},
         {'N': 1, 'W': 2, 'Q': 0},
         {'W': 2, 'S': 1, 'Q': 0}]

loc = 1
while True:
    # for direction in exits[loc].keys():
    #     availableExits += direction + ', '
    # Use .join() instead for efficiency
    availableExits = ', '.join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break

    direction = input('Available exits are ' + availableExits + ': ').upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print('You cannot go in that direction')

