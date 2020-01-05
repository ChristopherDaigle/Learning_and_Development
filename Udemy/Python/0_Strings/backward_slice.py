# Backward slicing
                                                        #-65432109876543210987654321
                                                        # 01234567890123456789012345
letters = "".join(sorted('qwertyuiopasdfghjklzxcvbnm')) # abcdefghijklmnopqrstuvwxyz
# print(letters)
# for i, a in enumerate(sorted('qwertyuiopasdfghjklzxcvbnm')):
#     print(i+1, a)
# print({a: i+1 for i, a in enumerate(sorted('qwertyuiopasdfghjklzxcvbnm'))})

# Start value of index 25, stop value up to index 0, counting backward by one®
backwards = letters[25:0:-1]    # zyxwvutsrqponmlkjihgfedcb
print(backwards)

backwards = letters[25:-1:-1]    # nothing
print(backwards)

backwards = letters[25::-1]    # zyxwvutsrqponmlkjihgfedcba
print(backwards)

backwards = letters[::-1]    # zyxwvutsrqponmlkjihgfedcba
print(backwards)

# Create a slice to produce:
# qpo
print(letters[16:13:-1])
print(letters[-12:-9][::-1])
# edbca
print(letters[4::-1])
# Last 8 characters in reverse order
print(letters[-1:-9:-1])    # zyxwvuts

# Idioms
#
# Return last n items in a sequence
print(letters[-4:])  # n = 4
# Last item
print(letters[-1])
print(letters[:1])
print(letters[0])
mt_string = ""
print(mt_string[:1])    # Good for getting first item in sequence without the code crashing
# print(mt_string[0])    # Crashes
