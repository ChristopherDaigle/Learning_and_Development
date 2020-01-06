age = int(input("How old are you: "))

# if age >= 16 and age <= 65:
if 16 <= age <= 65:
    print("Have a good day at work")
# age = int(input("How old are you: "))
if (age < 16) or (age > 65):
    print("Enjoy your free time")
else:
    print("Have a good day at work")

# if 16 > age < 65:
#     print("Enjoy your free time")
# else:
#     print("Have a good day at work")

x = "false"
if x:
    print("x is true")

x = input("Please enter text")
if x:
    print('You entered "{}'.format(x))
else:
    print("You didn't enter anything")

print(not False)
print(not True)

age = int(input("How old are you: "))
if not(age < 18):
    print("You are old enough to vote")
    print("Please put an 'X' in the box")
else:
    print("Please come back in {0} years.".format(18 - age))

parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print("Give me an {}, Bob.".format(letter))
else:
    print("I don't need that letter.")
