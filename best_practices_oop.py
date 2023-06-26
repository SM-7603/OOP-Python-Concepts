class Item:
    # down here, we've made put in these extra parameters (apart from self - which is there, to let the method know, for which instance its being executed for) to make them a requirement for creating an instance...
    # important side-notes: just because we're using the __init__ method doesn't mean that we can't differentiate b/w mandatory & non-mandatory parameters...
    # eg. if we don't know know the quantity for an item, then we set a default value inside the method itself, thereby making the parameter optional...
    def __init__(self, name, price, quantity=0):
        # what we've done now is define the attributes for each instance dynamically using the "self" parameter (because we know how self works in python from the previous file/example)
        # note for self - the stuff on the left {self.name,price,quantity} are the attributes and the stuff on the right are the parameters that the method receives from the instances...
        self.name = name
        self.price = price
        self.quantity = quantity
        # it's best practice to assignment the attributes inside the constructor

    def calculate_total_price(self, x, y):
        return x * y

# In terms of best practices in OOP, there are few problems that we've done here (below)

# 1. There aren't any set of rules for the attributes that we would like to pass in to instantiate an instance successfully.
# Meaning, what we've done here is hardcoded each attribute (i.e - for every item {item1, item2, item3, item4...} we would have to type in the attribute each time we create an instance TT_TT)

# Proposition:
# What if we could declare in a class that for every instance that we create, name, price & quantity must be passed.

# create constructor functions: (why?)
# Solution => create a special method - (__init__) == constructor
# these methods that start & end with these double underscores (__magicMethods__) are also known as magic methods

# More about the __init__ method (constructor):
# This is something that will be always executed (per instance) if its defined a class and an instance in created.


item1 = Item("Phone", 100)


item2 = Item("Laptop", 1000)


print(f"Item 1:")
print(f"Attribute 1 value: {item1.name}")
print(f"Attribute 2 value: {item1.price}")
print(f"Attribute 3 value: {item1.quantity}")
print(f"Item 2:")
print(f"Attribute 1 value: {item2.name}")
print(f"Attribute 2 value: {item2.price}")
print(f"Attribute 3 value: {item2.quantity}")
