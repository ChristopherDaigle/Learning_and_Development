__author__ = 'dev'

age = 33
print('My age is ' + str(age) + ' years.')
print()

# Replacement fields
print("My age is {0} years.".format(age))
print()
print("There are {0} days in, {1}, {2}, {3}, {4}, {5}, {6}, and {7}.".format(31,
        "January", "March", "May", "July", "August", "Ocrober", "December"))
print()

print("""January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28,30,31))
print()

# %d is an integer
print("My age is %d years" % age)
print()
print("My age is %d %s, %d %s" % (age, "years", 1, "months"))

# The number after the percent and before the d tells it the number of spaces
# to use so that the formatting will be nice
for i in range(1,12):
    print("No. %2d squared is %4d and cubed is %4d" % (i, i**2, i ** 3))
print()

# Specify the precisions of a number
print("Pi is approximately %12f" % (22/7))
print()
# Space after the decmial in 12.XX tells us the precision
print("Pi is approximately %12.50f" % (22/7))
# These are the numbers after the decimal, there are 50 of them
print(len('14285714285714279370154144999105483293533325195312'))
