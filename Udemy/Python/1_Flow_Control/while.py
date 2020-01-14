import random

for i in range(10):
    print("i is now {}".format(i))
print()
i = 0
while i < 10:
    print("i is now {}".format(i))
    i += 1
print()
# available_exits = ['east', 'north east', 'south']
# chosen_exit = ""
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")
#     if chosen_exit.lower() == "quit":
#         print("Game Over")
# print("Aren't you glad you got out of there!")
# print()
highest = 1000
answer = random.randint(1, highest)
guess = 0   # initiaize to any number outside of the valid range
print("Please guess a number between 1 and {}: ".format(highest))
while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    if guess < answer:
        print("Please guess higher")
    elif guess > answer:
        print('Please guess lower')
    else:
        print("Well done! You've guessed it.")
