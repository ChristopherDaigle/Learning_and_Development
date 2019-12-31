# Backward slicing
                                                        #-12345678901234567890123456
                                                        # 01234567890123456789012345
letters = "".join(sorted('qwertyuiopasdfghjklzxcvbnm')) # abcdefghijklmnopqrstuvwxyz
# print(letters)
# for i, a in enumerate(sorted('qwertyuiopasdfghjklzxcvbnm')):
#     print(i+1, a)
# print({a: i+1 for i, a in enumerate(sorted('qwertyuiopasdfghjklzxcvbnm'))})

# Start value of index 25, stop value up to index 0, counting backward by one
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
# edbca
print(letters[4::-1])
# Last 8 characters in reverse order
print(letters[-1:-9:-1])    # zyxwvuts
