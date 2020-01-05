# Python has three numeric types:
#
# 1. int: -1
# Python 3 has no integer max size
#
# 2. float: -1.0
# Max value is: 1.7976931348623157e+308
# Min value: 2.2250738585072014e-308
# 52 digits of precision
# Python 3 also has a "Decimal" data type which is more precise
#
# 3. complex: i ** 2

a = 12
b = 3

print(a + b)    # 15
print(a - b)    # 9
print(a * b)    # 36
print(a / b)    # 4.0
print(a // b)   # 4 integer division, rounded down to -\inf
print(a % b)    # 0, modulo, remainder after integer division

print()
# Won't work because of being a floating point value
# for i in range(1, a / b):
for i in range(1, a // b):
    print(i)

print(a ** 2)
print()
# Follow's order of operations
print(a + b / 3 - 4 * 12)
print(a + (b / 3) - (4 * 12))
print()

# Sequence: ORDERED set of items
# "Hello World" is a sequence of 11 items, each are string characters
# ['computer', 'monitor', 'keyboard', 'mouse', 'mouse pad'] is a sequence of 5 items, each are strings, which are
# also sequences themselves - a list may be a sequence of sequences
computer_parts = ['computer', 'monitor', 'keyboard', 'mouse', 'mouse pad']
print(computer_parts[1])   # 'monitor'
print(computer_parts[1][0])    # 'm'
