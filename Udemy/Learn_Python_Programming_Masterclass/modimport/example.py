# print(dir())
# # print(dir(__builtins__))
# for m in dir(__builtins__):
#     print(m)

import shelve

print(dir())
print("=" * 40)

for i in dir(shelve):
    print(i)
print("=" * 40)

for obj in dir(shelve.Shelf):
    if obj[0] != '_':
        print(obj)
print("=" * 40)

help(shelve)
print(shelve.__doc__)
