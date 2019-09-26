__author__ = 'dev'

# shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']
# for item in shopping_list:
#     if item == 'spam':
#         print('I am ignoring ' + item)
#         continue
#
#     print('Buy ' + item)
# print()
#
# for item in shopping_list:
#     if item == 'spam':
#         print('I am ignoring ' + item +' and stopping the shopping list')
#         break
#
#     print('Buy ' + item)
# print()


meal = ['egg', 'bacon', 'spam', 'sausages']
# # This for loop is bad because it fails to run if 'spam' is not in the list -> nasty_food_item never gets assigned
# for item in meal:
#     if item == 'spam':
#         nasty_food_item = item
#         break
#
# if nasty_food_item:
#     print("Can't I have anything without spam in it?")

# # This loop is better, but 'nasty_food_item' may never get assigned and then the loop runs,
# # but the variable is unnecessary
# for item in meal:
#     if item == 'spam':
#         nasty_food_item = item
#         break
#
# if nasty_food_item == 'spam':
#     print("Can't I have anything without spam in it?")

# This loop is even better, notice that 'nasty_food_item' is defined outside of the loop
# nasty_food_item = ''
# for item in meal:
#     if item == 'spam':
#         nasty_food_item = item
#         break
#
# if nasty_food_item == 'spam':
#     print("Can't I have anything without spam in it?")

# Using else in the for loop:
nasty_food_item = ''
for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
else:
    print("I'll have a plate of that, then, please.")
if nasty_food_item == 'spam':
    print("Can't I have anything without spam in it?")
print()

meal = ['egg', 'bacon', 'beans', 'sausages']
nasty_food_item = ''
for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
    else:
        nasty_food_item = ''
        print("I'll have a plate of that, then, please.")

if nasty_food_item == 'spam':
    print("Can't I have anything without spam in it?")
print()
