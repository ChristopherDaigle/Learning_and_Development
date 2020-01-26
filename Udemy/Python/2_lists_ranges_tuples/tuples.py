t = "a", "b", "c"   # This is a tuple even though there is no parenthesis
print(t)

print("a", "b", "c")
print(("a", "b", "c"))  # Necessary to include parenthesis for printing if desiring a tuple

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayehm", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)
print()
for i in range(len(metallica)):
    print(metallica[i])
print()

# Tuples are immutable - you can not change the values within them (directly)
try:
    metallica[0] = "Master of Puppets"  # Give error
except TypeError:
    print("ERROR: Tuples don't support item assignment")

# But we can assign new objects to the variable (recreate the tuple with reference to the previous):
imelda = imelda[0], "Imelda May", imelda[2]     # Note: Python evaluates the RHS of the expression (=) first
print(imelda)

# Immutable: you can't change the contents of an object once you've created it
# BUT it doesn't mean that your variable cant be assigned a new object of that type

metallica2 = ["Ride the Lightning", "Metallica", 1984]
print(metallica2)
metallica2[0] = "Master of Puppets"
print(metallica2)
print()
title, artist, year = imelda    # Tuple unpacking
print(title)
print(artist)
print(year)
