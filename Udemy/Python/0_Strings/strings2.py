#         43210987654321
#         01234567890123
parrot = "Norwegian Blue"

print(parrot)

print(parrot[3])
print(parrot[4])
# print()
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])
print()
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])
print()
print(parrot[3 - 14])
print(parrot[4 - 14])
# print()
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])
print()
# Slice from index 0 up to (not including) 6
print(list(range(0, 6)))
print(parrot[0:6])  # Norweg
print(parrot[3:5])  # we
print(parrot[0:9])  # Norwegian
# The first value is the position to start at, but will start at 0 if none
# is provided
print(parrot[:9])   # Norwegian
# The second value is the stop position (up to), but will stop at last if
# none is provided
print(parrot[10:14])
print(parrot[10:])

print(parrot[:6] + parrot[6:])
print(parrot[:])

print(parrot[-4:2])     # Prints nothing as this says the end is before the start, index -4 is after index 2
print(parrot[-4:-2])    # Bl
print(parrot[-4:12])    # Bl

# Introducing a step
print(parrot[0:6:2])    # Nre ; starts at 0, goes up to 6, and does so in steps of 2
print(parrot[0:6:3])    # Nw; starts at 0, goes to 6, and does so in steps of 3

number = "9,223,372,036,854,775,807"
print(number[1::4])     # ,,,,,, ; Starts at 1, goes to end, and does so in steps of 4
number = "9,223;372:036 854,775;807"
print(number[1::4])     # ,;: ,; ; Starts at 1, goes to end, and does so in steps of 4
separators = number[1::4]
print(separators)
values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
