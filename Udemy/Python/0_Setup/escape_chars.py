# The escape character
split_string = "This string has been \nsplit over\nseveral\nlines"
print(split_string)
print()
tabbed_string = "1\t2\t3\t4\t5"
print(tabbed_string)
print()

print('The pet shop owner said "No, no, \'e\'s uh, ... he\'s resting".')
print("The pet shop owner said \"No, no, \'e\'s uh, ... he's resting\".")
print("""The pet shop owner said "No, no, 'e's uh, ... he's resting".""")
print("""The pet shop owner said "No, no, \
'e's uh, ... he's resting".""")
print()

print(split_string)
print()
another_split_string = """This string has been
split over
several
lines"""
print(another_split_string)
print()
yass = another_split_string = """This string has been \
split over \
several \
lines"""
print(yass)
print()
# Can see problems with \U, \t, \n
# print("C:\Users\tim\notes.txt")
print("C:\\Users\\tim\\notes.txt")
# Raw string:
print(r"C:\Users\tim\notes.txt")
print()