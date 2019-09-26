__author__ = 'dev'

# # Tuples are an ordered set of data
# # A tuple is imutable, unlike lists
# # Tuples are not necessarily parenthesis where lists are square brackets
# # but parenthesis are often used to remove ambiguity
#
# t = 'a', 'b', 'c'
# # t is a tuple
# print(t)
# # but this print statement doesn't display as a tuple
# print('a', 'b', 'c')
# # so we add parenthesis to set the items as a tuple
# print(('a', 'b', 'c'))

# Notice we have different data types on one line
welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984
#
# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
#
# # This won't work as tuples are imutable
# # metallica[0] = 'Master of Puppets'
# # But you can do other things... like completely recreating it
# # (Because expressions on the RHS of the "=" are always evaluated before the LHS)
# imelda = imelda[0], "Imelda May", imelda[2]
# print(imelda)
# # A type being imutable means that you can't change the contents of an object once you've created it
# # But it doesn't mean that your variable, in this case a tuple, can't be assigned a new object of that type
#
# # In the list, we can easily change the items in the list because it is mutable
# # Note however, lists are meant to hold objects of the same type (homogeneous),
# # tuples are useful for heterogenous items
metallica2 = ["Ride the Lightning", "Metallica", 1984]
# print(metallica2)
# metallica2[0] = "Master of Puppets"
# print(metallica2)
# Good to use tuples for things you dont think shou'd ever be changed in your code (like SSN or album names, etc)
imelda = "More Mayhem", "Imelda May", 2011

# # Here is tuple unpacking!
# title, artist, year = imelda
# print(title)
# print(artist)
# print(year)
# print()
#
# title, artist, year = metallica2
# print(title)
# print(artist)
# print(year)
# print()
#
# # # This fails
# metallica2.append('Rock')
# # title, artist, year, = metallica2
# # print(title)
# # print(artist)
# # print(year)
# # # This succeeds
# title, artist, year, genre = metallica2
# print(title)
# print(artist)
# print(year)

# # A tuple can contain elements which are also tuples
# imelda = "More Mayhem", "Imilda May", 2011, (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Walts"))
# print(imelda)
#
# title, artist, year, tracks = imelda
# print(title)
# print(artist)
# print(year)
# print(tracks)
# print()
#
# imelda = "More Mayhem", "Imilda May", 2011, (1, "Pulling the Rug"),\
#          (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Walts")
# # We need to make sure we have the number of elements in the tuple or we wont be able to assign them to variables
# title, artist, year, track1, track2, track3, track4 = imelda
#
# print(title)
# print(artist)
# print(year)
# print(track1)
# print(track2)
# print(track3)
# print(track4)
# print()

# imelda = "More Mayhem", "Imilda May", 2011, 1, "Pulling the Rug", \
#          2, "Psycho", 3, "Mayhem", 4, "Kentish Town Walts"
# # This will cause a failure now because we have indicated tuple unpacking with a number of variables less than
# # the number of elements in the tuple
# title, artist, year, track1, track2, track3, track4 = imelda
#
# print(title)
# print(artist)
# print(year)
# print(track1)
# print(track2)
# print(track3)
# print(track4)
# print()

"""Challenge
Given the tuple below that represents the Imelda May album 'More Mayhem', write
 code to print the album details, followed by a listing of all the tracks in the album.
 
 Indent the tracks by a single tav stop when printing them (remember that you can pass more than one item
 to the print function, separating them with a comma"""
# imelda = "More Mayhem", "Imilda May", 2011, (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Walts"))
# print(imelda)
#
# # My solution
# album, artist, year, tracks = imelda
# print(album)
# print(artist)
# print(year)
# for i in tracks:
#     print('\t', i)
# print()
#
# # print(album + ', ' + artist + ', ' + str(year) + ', ', str(['{}'.format(i) for i in tracks]))
# # Tim's solution
# album, artist, year, tracks = imelda
# print(album)
# print(artist)
# print(year)
# for song in tracks:
#     track, title = song
#     print('\tTrack number {}, Title: {}'.format(track, title))
# print()

# Addressing a tuple with a list as an element:
imelda = "More Mayhem", "Imilda May", 2011, (
    [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Walts")])
print(imelda)

# Select the element of the tuple that is a list
imelda[3].append((5, "All For You"))

album, artist, year, tracks = imelda
# After performing tuple unpacking, we can append only that element instead of the previous method
tracks.append((6, "Eternity"))

print(album)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print('\tTrack number {}, Title: {}'.format(track, title))
print()
