__author__ = 'dev'

""" Create a program that takes some text and returns a list of all
the characters in the text that are not vowels, sorted in alphabetical order.

You can either enter the text from the keyboard or
initialize a string variable with the string."""
# My answer:
vowels = ('a', 'e', 'i', 'o', 'u')
userString = set(input('Enter a string: '))

consonantsSplitUserString = userString.difference(vowels)
orderedConsonants = sorted(consonantsSplitUserString)

print(orderedConsonants)
print('=' * 50)
# Tim's answer:
sampleText = "Python is a very powerful language."

vowels = frozenset("aeiou")
# vowels = {"a", "e", "i", "o", "u"}
finalSet = set(sampleText).difference(vowels)
print(finalSet)

finalList = sorted(finalSet)
print(finalList)
