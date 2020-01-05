print("Today is a good day to learn Python")
print('Python is fun')
print("Python's strings are easy to use")
print('We can even include "quotes" in strings')
print("Hello" + " world")

greeting = "Hello"
name = "Chris"
print(greeting + ' ' + name)

# dynamic_name = input("Please enter your name: ")
# print(greeting + ' ' + dynamic_name)

age = 33
print(age)
# Python returns the type of the value, not necessarily the type of the variable
print(type(greeting))
print(type(age))
# Python allows us to change the type of a variable simply by replacing the value
# NOTE: This is not possible in many other languages (e.g. Java, C, etc.)
age = "2 years"
print(age)
print(type(age))
age = 33
# In python its more helpful to say we've rebound the
# label age to the value "2 years"

# It can be helpful to think of a variable as a name or label that is bound
# to a value

# THIS DOES NOT MEAN THAT PYTHON IS A WEAKLY TYPED LANGUAGE
# Weak typed language: program doesn't care what type a variable is
# String typed: program depends on the variable's type

# An example of Python being strongly typed:
age_in_words = "2_years"
# print(name + " is " + age + " years old")   # Error, let's address with an 'f-string'
print(name + f" is {age} years old")
print(type(age))

print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")
