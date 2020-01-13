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
highest = 10
answer = random.randint(1, highest)
guess = int(input("Please guess a number between 1 and {}: ".format(highest)))
if guess != answer:
    if guess < answer:
        guess = int(input("Please guess higher: "))
    else:
        guess = int(input("Please guess lower: "))
else:
    print("Well done! You've guessed it")
