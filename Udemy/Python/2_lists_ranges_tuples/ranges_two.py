decimals = range(0, 100)
my_range = decimals[3:40:3]
print(my_range == range(3, 40, 3))
print(range(0, 5, 2) == range(0, 6, 2))
print(list(range(0, 5, 2)))
print(list(range(0, 6, 2)))

r = range(0, 100)
print(r)

for i in r[::-2]:
    print(i)
print()
for i in range(99, 0, -2):
    print(i)
print()
print(range(0, 100)[::-2] == range(99, 0, -2))
print()
back_string = "egaugnal lufrewop yrev a si nohtyP"
print(back_string[::-1])
print()
r = range(0, 10)
for i in r[::-1]:
    print(i)

# Challenge
o = range(0, 100, 4)    # defines a sequence generation from 0 up to 100 by 4s
print(o)    # range(0, 100, 4)
p = o[::5]
print(p)    # range(0, 100, 20)
print(list(p))  # [0, 20, ... 80]
