for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print()

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

print()

print("Pi is approximately {0:12}".format(22 / 7))      # Defaults to 15 decimals
print("Pi is approximately {0:12f}".format(22 / 7))     # Defaults to FP precision of 6 digits after the decimal points
print("Pi is approximately {0:12.50f}".format(22 / 7))  # Specify FP but also specifiy precision of 50 points
print("Pi is approximately {0:52.50f}".format(22 / 7))  # Note that Python sets precision above field width (eg line 13)
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:72.50f}".format(22 / 7))
print("Pi is approximately {0:<72.54f}".format(22 / 7))
print()
for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
