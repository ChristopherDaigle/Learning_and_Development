shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shopping_list:
    if item == "spam":
        print("I am ignoring " + item + ".")
        continue    # Stops processing that iterator and goes to the next iterator in the sequence
    print("Buy " + item)
print()
for item in shopping_list:
    if item == "spam":
        print("I am ignoring " + item + ".")
        break    # Stops processing the iterator completely
    print("Buy " + item)
print()
for i in range(0, 3):
    for item in shopping_list:
        if item == "spam":
            print("I am ignoring " + item + ".")
            break    # Stops processing the iterator completely, thus breaking the loop, but not all loops
        print("Buy " + item)
    print(i)
print()
for i in range(0, 3):
    print(i)
    for item in shopping_list:
        if item == "spam":
            print("I am ignoring " + item + ".")
            break    # Stops processing the iterator completely, thus breaking the loop, but not all loops
        print("Buy " + item)
print("=" * 19)
print()

nasty_food_item = ''
meal = ["egg", "bacon", "spam", "sausages"]
for item in meal:
    if item == "spam":
        nasty_food_item = item
        break
else:   # else can follow the if OR the for statement; this one follows the for
    print("I'll have a plate of that, then, please.")

if nasty_food_item == "spam":
    print("Can't I have anything without spam in it?")
# try:
#     if nasty_food_item:
#         print("Can't I have anything without spam in it?")
# except NameError:
#     print("There was no spam!")
