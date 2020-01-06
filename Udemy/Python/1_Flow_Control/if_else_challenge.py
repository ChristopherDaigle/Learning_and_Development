name = input("What is your name: ")
age = int(input("How old are you, {}: ".format(name)))

if 18 <= age <= 31:
    print("Welcome to holiday")
else:
    if 18 > age:
        print("Please come back in {} years.".format(18 - age))
    else:   # must be greater than 31
        print("You are {} too many years old.".format(age - 31))
