number = "9,223,372,036,854,775,807"
cleaned_number = ""

for char in number:
    if char in "1234567890":
        cleaned_number += char

new_number = int(cleaned_number)
print("The number is now {}".format(new_number))
print()
for state in ["not pinin'", "no more", "a stiff", "bereft of life"]:
    print("This parrot is " + state + ".")
    # print("This parrot is {}.".format(state))
print()
for i in range(0, 100, 5):  # count from zero up to 100 in steps of 5
    print("i is {}".format(i))
print()
for i in range(1, 13):
    for j in range(1, 13):
        print("{0} times {1:>2} is {2:>3}".format(i, j, i * j))
    print("=" * 18)
