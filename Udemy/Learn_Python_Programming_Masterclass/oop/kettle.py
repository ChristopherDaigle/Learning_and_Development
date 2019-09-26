__author__ = 'dev'
# A class can be thought of as a template from which objects can be created
# Here is a method: def __init__(self, make, price)
# When we create objects of this Kettle class, they all have a make and a price
# They don't have to have the same name or the same price
# An instance is a particular element of an object created from a class definition
# Each instance of the class will have its own values for name and price


class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


# Here I am creating an instance of the Kettle class
kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.75)
print("=" * 50)
print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

"""
Class: template for creating objects. All objects created using the same class will have the same characteristics
Type: Equivalent to a class (in Python)
Object: an instance of a class
Instantiate: create an instance of a class (an object)
Attribute: a variable bound to an instance of a class
"""
# What is "self"? It is a reference to the instance of the class
print("=" * 50)
print(hamilton.on)
# Kettle is constructed so that it .on is initially False, so when we call hamilton.on, we see False
# but if we call .switch_on(), .on becomes True from the switch_on() method
hamilton.switch_on()
print(hamilton.on)
print("=" * 50)
# Here we use the .switch_on() method on the class to change the attributes of an instance
Kettle.switch_on(kenwood)
print(kenwood.on)
kenwood.switch_on()

print("=" * 50)
kenwood.power = 1.5
# This is a data attribute
# This is not usually a good idea, but its possible
print(kenwood.power)
# print(hamilton.power) # This fails because we didn't define it as we did for kenwood.power = 1.5
print("=" * 50)
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
print("=" * 50)
# Namespace
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
print("=" * 50)
print("Switch to atomic power")
Kettle.power_source = "atomic"
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
print("=" * 50)
# Namespace
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
print("Switch kenwood to gas")
kenwood.power_source = "gas"
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
print("=" * 50)
# Namespace
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
