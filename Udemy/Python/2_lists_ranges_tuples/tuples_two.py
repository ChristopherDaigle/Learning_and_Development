welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayehm", "Imilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984
metallica2 = ["Ride the Lightning", "Metallica", 1984]

# title, artist, year = imelda    # Tuple unpacking
# print(title)
# print(artist)
# print(year)

# Lists can cause problems though when you try to do this
# For example, if the list is ever made a different length than it may be defined elsewhere, say with .append()
metallica2.append("Rock")
try:
    title, artist, year = metallica2
    print(title)
    print(artist)
    print(year)
except ValueError:
    print("ERROR: too many values to unpack (expected 3)")
print()
# There is no appending a tuple:
try:
    imelda.append("Jazz")
except AttributeError:
    print("ERROR: 'tuple' object has no attribute 'append'")
print()

imelda = "More Mayehm", "Imilda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
print(imelda)
title, artist, year, tracks = imelda
print()
print(title)
print(artist)
print(year)
# print(tracks)
# print()
for track, song_title in tracks:
    print("\t", track, song_title)
print()

imelda = "More Mayehm", "Imilda May", 2011, 1, "Pulling the Rug", 2, "Psycho", 3, "Mayhem", 4, "Kentish Town Waltz"
# Note the importance of datatype structure:
try:
    title, artist, year, track1, track2, track3, track4 = imelda
except ValueError:
    print("ERROR: too many values to unpack (expected 7)")
print()

# Note that just because a tuple cannot be changed, if an element of a tuple is mutable, that element in the
# tuple can be changed
imelda = "More Mayehm", "Imilda May", 2011, (
    [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")])
# The element at index 3 is the tuple of list of tuples of tracks and song titles
imelda[3].append((5, "All For You"))    # We can append a track and song title here
title, artist, year, tracks = imelda
print()
print(title)
print(artist)
print(year)
# print(tracks)
# print()
for track, song_title in tracks:
    print("\t", track, song_title)
print()
