# ip_address = input("Please enter an IP address: ")
# print(ip_address.count("."))

parrot_list = ["not pinin'", "no more", "a stiff", "bereft of life"]

parrot_list.append("A Norwegian Blue")

for state in parrot_list:
    print("This parrot is " + state)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
# numbers.sort()    # This creates a new variable of the sorted numbers
print(sorted(numbers))  # This displays a sorted version of the number but doesnt make a new variable
print(numbers)
numbers_in_order = sorted(numbers)  # This assigns numbers_in_order to the ordered list of numbers
print(numbers)
print(numbers_in_order)

if numbers == numbers_in_order:
    print("The lists are equal")
else:
    print("The lists are not equal")    # The lists will not be equal as the order of a list matters

if numbers_in_order == sorted(numbers):
    print("The lists are equal")    # The lists will be equal as the order of a list matters
else:
    print("The lists are not equal")