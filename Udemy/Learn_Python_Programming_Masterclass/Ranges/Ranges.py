__author_ = 'dev'

# myList = list(range(1, 11))
# even = list(range(0,11,2))
# odd = list(range(1,11,2))
# print(myList)
# print(even)
# print(odd)
#
# # Ranges take up the same amount of memory, regardless of their "space" (i.e. 1-10 VS 1-10000)
# # but lists take up more
# range(0,10)

# myString = 'abcdefghijklmnopqrstuvwxyz'
# print(myString.index('e'))
# print(myString[4])
#
# smallDecimals = range(0,10)
# print(smallDecimals)
# print(smallDecimals.index(3))
#
# odd = range(1, 10000, 2)
# print(odd)
# print(odd[985])
#
# sevens = range(7, 1000000, 7)
# x = int(input('Please enter a number less than one million: '))
# if x in sevens:
#     print('{} is divisible by seven.'.format(x))
# else:
#     print('That value is not divisible by seven.')
#
# myRange = smallDecimals[::2]
# print(myRange)
# print(myRange.index(4))

# decimals = range(0, 100)
# print(decimals)
#
# myRange = decimals[3:40:3]
# print(myRange)
#
# for i in myRange:
#     print(i)
#
# print('=' * 40)
#
# for i in range(3, 40, 3):
#     print(i)
#
# print( myRange == range(3, 40, 3))

# # This returns true based on the output
# print(range(0, 5, 2) == range(0, 5, 2))
# # These are plainly the same output
# print(list(range(0, 5, 2)))
# print(list(range(0,6,2)))
#
# r = range(0, 100)
# print(r)
#
# for i in r[::-2]:
#     print(i)
# print('=' *50)
#
# for i in range(99,0, -2):
#     print(i)
# print('='*50)
#
# print(range(0,100)[::-2] == range(99, 0, -2))
#
# # Wont return any output because the range must be in reverse, that is
# # range(a,b, -i) only returns an output when a>b and |i| <a
# for i in range(0,100,-2):
#     print(i)

# backString = "egaugnal lufrewop yrev a si nohtyP"
# print(backString)
# print(backString[::-1])
#
# r = range(0,10)
# for i in r[::-1]:
#     print(i)
"""Challenge"""
# Experiment with different ranges and slices to get a feel for how they work.
# Remember that you can print the range as well as iterating through it to print
# its values, to check that your ranges are what you expected.
# You may also want to include things like.
#
o = range(0, 100, 4)
print(o)
p = o[::5]
print(p)
for i in p:
    print(i)

# and see if you can work out what will be printed before running the program. If you are unsure, use a
# for loop to print out the values of o to see why p returns what it does.

print()

pList = list(p)
iterP = iter(pList)

for i in range(len(pList)):
    print(next(iterP))
