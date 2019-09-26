__author__ = 'dev'

# greeting = "Chris"
# _myName = "Patrick"
# Chris33 = 'Good'
# Chris_Was_32 = "Hello"
# Greeting = "There"
# print(Chris_Was_32 + ' ' +  greeting)
# print()
#
# age = 33
# print(age)
# print()
#
# print(greeting + age)

a = 12
b = 3
#
# # Integer
# print(a + b)
# print()
# # Integer
# print(a - b)
# print()
# # Integer
# print(a * b)
# print()
# # Float
# print(a / b)
# print()
# # Integer
# print(a // b)
# print()
# # Remainder
# print(a % b)

# for i in range (1,4):
#     print(i)
# print()
# # Doesnt work because a/b is a float
# # for i in range(1, a/b):
# #     print(i)
#
# # Does work because a//b is an integer
# for i in range(1, a//b):
#     print(i)
# print()
#
# # Nothing crazy, just PEMDAS
# print(a + b // 3 - 4 * 12)
# print(12 + (1) - (48))

# a = 12
# b = 3
# c = a + b
# d = c / 3
# e = d - 4
#
# print(e * 12)

parrot = "Norwegian Blue"
print(parrot)
print()
print(parrot[3])
print()
print(parrot[0])
print()

print(parrot[-1])
# Prints the first character up to exclusive of the 6th character (up to but not including)
print(parrot[0:6])
print(parrot[:6])
print(parrot[6:])
print(parrot[-4:-2])
# Extract all the characters from index 0 up to index 6 in steps of 2
print(parrot[0:6:2])
print(parrot[0:6:3])

number = "9,223,372,036,854,775,807"
print(number[1::4])

numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[0::3])
print(numbers[0::4])

string1 = "he's "
string2 = "probably "
print(string1 + string2)
print("he's probably pining")
print("hello"*5)
print(5*"hello")
print("hello" * (5+4))
print("hello" *5 +' 4')

today = "friday"
print("day" in today)
print("parrot" in "fjord")
