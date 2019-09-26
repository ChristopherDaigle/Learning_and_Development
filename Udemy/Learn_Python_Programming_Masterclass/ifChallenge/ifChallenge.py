# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person
# is the right age to on a 18-30 holiday (they must be
# over 18 and under 31).
# If they are, welcome them to the holiday, otherwise print
# a (polite) message refusing them entry.

name = input('Enter your name: ')
age = int(input('How old are you, {0}? '.format(name)))

if (age < 18) or (age > 30):
    print("Sorry {0}, you can't go on holiday.".format(name))
    if age < 18:
        print('You can come back in {0} years to go on the holiday.'.format(18-age))
else:
    print('Welcome to the 18-30 holiday, {}!'.format(name))
