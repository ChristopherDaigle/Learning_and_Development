__author__ = 'Chris'

"""
    Open and Read
"""
## Pythonic version of opening a file
#
# jabber = open("sample.txt", 'r')
#
# for line in jabber:
#     if 'jabberwock' in line.lower():
#         # The print(... , end ='') is not required in Python, but is helpful for knowing the end of line (EOL)
#         # characters
#         print(line, end='')
#
# jabber.close()

## Other version of inputing a file
# with open('sample.txt', 'r') as jabber:
#     for line in jabber:
#         if 'JAB' in line.upper():
#             print(line, end='')

## Other versions of reading the lines in the file
# with open('sample.txt', 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end ='')
#         line = jabber.readline()

## Another example
# with open('sample.txt', 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines:
#     print(line, end='')

## Another example
# with open('sample.txt', 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines[::-1]:
#     print(line, end='')

## Another example
with open('sample.txt', 'r') as jabber:
    lines = jabber.read()

for line in lines[::-1]:
    print(line, end='')
